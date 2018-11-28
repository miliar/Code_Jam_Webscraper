#include <iostream>
#include <string>
#include <map>
using namespace std;

unsigned int code[128];
char table[128][128];
int sgn[128][128];

void init() {
  code['1'] = 0;
  code['i'] = 1;
  code['j'] = 2;
  code['k'] = 3;

  table['1']['1'] = '1'; sgn['1']['1'] = +1;
  table['1']['i'] = 'i'; sgn['1']['i'] = +1;
  table['1']['j'] = 'j'; sgn['1']['j'] = +1;
  table['1']['k'] = 'k'; sgn['1']['k'] = +1;
  
  table['i']['1'] = 'i'; sgn['i']['1'] = +1;
  table['i']['i'] = '1'; sgn['i']['i'] = -1;
  table['i']['j'] = 'k'; sgn['i']['j'] = +1;
  table['i']['k'] = 'j'; sgn['i']['k'] = -1;
  
  table['j']['1'] = 'j'; sgn['j']['1'] = +1;
  table['j']['i'] = 'k'; sgn['j']['i'] = -1;
  table['j']['j'] = '1'; sgn['j']['j'] = -1;
  table['j']['k'] = 'i'; sgn['j']['k'] = +1;
  
  table['k']['1'] = 'k'; sgn['k']['1'] = +1;
  table['k']['i'] = 'j'; sgn['k']['i'] = +1;
  table['k']['j'] = 'i'; sgn['k']['j'] = -1;
  table['k']['k'] = '1'; sgn['k']['k'] = -1;
}

int T, L, X;
string str;

unsigned int hash_fn(int i, int ijk, char ch, int sg) {
  unsigned int h = i;
  h |= ((unsigned int)ijk) << 14;
  h |= code[ch] << 16;
  if (sg < 0) h |= 1U << 18;
  return h;
}

map<unsigned int, bool> memory;
bool isReducible(int i, int ijk, char ch, int sg) {
  static int cache_hit = 0;
  static const char *target = "ijk";
  if (i >= L*X) return (ijk == 3);
  if (ijk >= 3) return false;
  unsigned int H = hash_fn(i, ijk, ch, sg);
  if (memory.find(H) == memory.end()) {
    sg *= sgn[ch][str[i%L]];
    ch = table[ch][str[i%L]];
    i++;
    if (sg > 0 && ch == target[ijk]) {
      if (isReducible(i, ijk + 1, '1', +1)) {  // split
        return (memory[H] = true);
      }
    }
    memory[H] = isReducible(i, ijk, ch, sg);
  } else {
#ifdef _DEBUG
    cout << "cache hit no. " << (++cache_hit) << endl;
#endif
  }
  return memory[H];
}

int main() {
  init();
  cin >> T;
  for (int t = 1; t <= T; t++) {
    memory.clear();
    cin >> L >> X >> str;
    cout << "Case #" << t << ": " << (isReducible(0, 0, '1', +1) ? "YES" : "NO") << endl;
  }
  return 0;
}
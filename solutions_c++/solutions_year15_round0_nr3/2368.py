#include <iostream>
#include <string>
using namespace std;

enum { q1 = 1, qI = 2, qJ = 3, qK = 4, qTRAP = 10 };

size_t N, L, X;
int current;
int lookingFor;
int lastLookingFor;
int lastEnded;
char seen[11] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
size_t whenSeen[11] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
const char nextToFind[] = { 0, 0, qJ, qK };
string word;

const int arr[5][5] =
{
  { 0, 0, 0, 0, 0 },
  { 0, q1, qI, qJ, qK },
  { 0, qI, -q1, qK, -qJ },
  { 0, qJ, -qK, -q1, qI },
  { 0, qK, qJ, -qI, -q1 }
};

char convertToEnum(char c)
{
  switch (c)
  {
    case 'i': return qI;
    case 'j': return qJ;
    case 'k': return qK;
    default: cerr << "THIS SOULD NEVER HAPPEN!\n";
  }
  return 0;
}

int mul(int a, int b)
{
  if (a * b > 0) return arr[a][b];
  else return -arr[abs(a)][abs(b)];
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin >> N;
  for (size_t i=0; i<N; ++i)
  {
    cin >> L;
    cin >> X;
    getline(cin, word);
    getline(cin, word);
    for (auto& c : word) c = convertToEnum(c);

    current = q1;
    lookingFor = qI;
    lastLookingFor = qTRAP;
    lastEnded = qTRAP;
    for (size_t att=0; att<X; ++att)
    {
      if (lookingFor == lastLookingFor)
      {
        if (seen[current+5])
        {
          if (lookingFor != qK)
          {
            current = qTRAP;
            break;
          }
          else
          {
            size_t cycleLen = att - whenSeen[current+5];
            for (size_t k=0; k<sizeof seen; ++k)
              seen[k] = 0;
            size_t iterations = (X - att - 1) / cycleLen;
            att += iterations * cycleLen;
          }
        }
        else
        {
          seen[current+5] = 1;
          whenSeen[current+5] = att;
        }
      }
      else
      {
        for (size_t k=0; k<sizeof seen; ++k)
          seen[k] = 0;
      }
      lastLookingFor = lookingFor;
      for (int c : word)
      {
        current = mul(current, c);
        if (current == lookingFor && lookingFor != qK)
        {
          current = q1;
          lookingFor = nextToFind[lookingFor];
        }
      }
    }
    if (current == qK && lookingFor == qK)
      cout << "Case #" << (i+1) << ": YES\n";
    else
      cout << "Case #" << (i+1) << ": NO\n";
  }

  return 0;
}
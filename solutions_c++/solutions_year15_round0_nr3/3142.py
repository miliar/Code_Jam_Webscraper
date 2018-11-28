#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* table[9][9] = {{"", "1", "i", "j", "k", "-1", "-i", "-j", "-k"},
         {"1", "1", "i", "j", "k", "-1", "-i", "-j", "-k"}, 
         {"i", "i", "-1", "k", "-j", "-i", "1", "-k", "j"}, 
         {"j", "j", "-k", "-1", "i", "-j", "k", "1", "-i"}, 
         {"k", "k", "j", "-i", "-1", "-k", "-j", "i", "1"},
         {"-1", "-1", "-i", "-j", "-k", "1", "i", "j", "k"}, 
         {"-i", "-i", "1", "-k", "j", "i", "-1", "k", "-j"}, 
         {"-j", "-j", "k", "1", "-i", "j", "-k", "-1", "i"}, 
         {"-k", "-k", "-j", "i", "1", "k", "j", "-i", "-1"}};

char* order[9]  = {"", "1", "i", "j", "k", "-1", "-i", "-j", "-k"};

int index(char* a) {
  for (int i = 0; i < 9; i++) {
    if (!strcmp(order[i], a)) {
      return i;
    }
  }
  return -1;
}

char* multiply(char* a, char* b) {
  int x = index(a);
  int y = index(b);  
  //printf("%d(%s), %d(%s) = %s\n", x, a, y, b, table[x][y]);
  return table[x][y];
}

char* evaluate(char* code) {
  int length = strlen(code);

  if (length == 1) {
    return code;
  }

  char temp[2];
  temp[0] = code[0];
  temp[1] = '\0';

  char* ch = temp;
  for(int i = 1; i < length; i++) {
    char tt[2] = {code[i], 0};
    ch = multiply(ch, tt);
  }

  return ch; 
}

void testcode1() {
  printf("%s\n", multiply("1", "-1"));
  printf("%s\n", multiply(multiply("i", "j"), "k"));
  printf("%s\n", multiply(multiply("-j", "i"), "j"));

  printf("%s\n", evaluate("kiijkiijkiij"));
  printf("%s%s%s\n", evaluate("jij"), evaluate("iji"), evaluate("jijiji"));
}

bool calc(int ind, char* string, int length);

void loop() {
  FILE* fp = fopen("small-attempt0.in", "rt");
  char line[40960];
  int T = 0;
  fscanf(fp, "%d", &T);
  printf("Total instance = %d\n", T);
  int ind = 1;
  while(!feof(fp)) {
    int L = 0, X = 0;
    fscanf(fp, "%d %d", &L, &X);
    if (L == 0 && X == 0)
      break;
    //printf("%d, %d\n", L, X);
   
    int length = L * X;
    char* line = (char*)malloc(length+1);
    memset(line, 0, length + 1);
    fscanf(fp, "%s", line);
    for (int i = 1; i < X; i++) {
      memcpy(&line[L * i], line, L);
    }

    bool result = calc(ind, line, length);  
    printf("Case #%d: %s\n", ind, (result) ? "YES" : "NO");

    ind += 1;
  }

  fclose(fp);
}

bool calc(int ind, char* string, int length) {
  if (length < 3) {
    return false;
  }
  else if (length == 3) {
    if (!strcmp(string, "ijk")) {
      return true;
    }
    else {
      return false;
    } 
  }

  char** cache = (char**)malloc(length*sizeof(char*));
  memset(cache, 0, length*sizeof(char*));

  char tp[2] = {string[length - 1], '\0'}, *temp = NULL;
  temp = tp;
  cache[length - 1] = tp;
  for (int i = length - 1; i > 0; i--) {
    char t[2] = {string[i-1], '\0'};
    temp = multiply(t, temp);
    cache[i-1] = temp;
  }

  char* ch = "";
  for(int i = 0; i < length - 2; i++) {
    char temp[2] = {string[i], '\0'};
    ch = multiply(ch, temp);
    if (ch[0] != 'i')
      continue;
    
    char* och = "";
    for (int j = i + 1; j < length - 1; j++) {
      char tone[2] = {string[j], '\0'};
      och = multiply(och, tone);
      if (och[0] != 'j')
        continue;

      if (cache[j+1][0] != 'k')
        continue;
      else
        return true;
    }
  }

  return false;
}

    
int main() {
  //testcode1();
  loop();
  return 0;
}

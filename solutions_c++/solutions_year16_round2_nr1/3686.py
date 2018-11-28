#include<iostream>
#include <string.h>

using namespace std;

bool has(int a[], int n)
{
    switch(n) {
        case 0:
           return a['Z'-'A'] > 0 && a['E' - 'A'] > 0 && a['R' - 'A'] > 0 && a['O' - 'A'] > 0;
        case 1:
           return a['O'-'A'] > 0 && a['N' - 'A'] > 0 && a['E' - 'A'] > 0;
        case 2:
           return a['T'-'A'] > 0 && a['W' - 'A'] > 0 && a['O' - 'A'] > 0;
        case 3:
           return a['T'-'A'] > 0 && a['H' - 'A'] > 0 && a['R' - 'A'] > 0 && a['E' - 'A'] > 1;
        case 4:
           return a['F'-'A'] > 0 && a['O' - 'A'] > 0 && a['U' - 'A'] > 0 && a['R' - 'A'] > 0;
        case 5:
           return a['F'-'A'] > 0 && a['I' - 'A'] > 0 && a['V' - 'A'] > 0 && a['E' - 'A'] > 0;
        case 6:
           return a['S'-'A'] > 0 && a['I' - 'A'] > 0 && a['X' - 'A'] > 0;
        case 7:
           return a['S'-'A'] > 0 && a['E' - 'A'] > 1 && a['V' - 'A'] > 0 && a['N' - 'A'] > 0;
        case 8:
           return a['E'-'A'] > 0 && a['I' - 'A'] > 0 && a['G' - 'A'] > 0 && a['H' - 'A'] > 0 && a['T' - 'A'] > 0;
        case 9:
           return a['N'-'A'] > 1 && a['I' - 'A'] > 0 && a['E' - 'A'] > 0;
        
    }
}

void decrement(int a[], int n)
{
    switch(n) {
        case 0:
           --a['Z'-'A']; --a['E' - 'A']; --a['R' - 'A']; --a['O' - 'A'];
           break;
        case 1:
           --a['O'-'A']; --a['N' - 'A']; --a['E' - 'A'];
           break;
        case 2:
           --a['T'-'A']; --a['W' - 'A']; --a['O' - 'A'];
           break;
        case 3:
           --a['T'-'A']; --a['H' - 'A']; --a['R' - 'A']; a['E' - 'A']-=2;
           break;
        case 4:
           --a['F'-'A']; --a['O' - 'A']; --a['U' - 'A']; --a['R' - 'A'];
           break;
        case 5:
           --a['F'-'A']; --a['I' - 'A']; --a['V' - 'A']; --a['E' - 'A'];
           break;
        case 6:
           --a['S'-'A']; --a['I' - 'A']; --a['X' - 'A'];
           break;
        case 7:
           --a['S'-'A']; a['E' - 'A']-=2; --a['V' - 'A']; --a['N' - 'A'];
           break;
        case 8:
           --a['E'-'A']; --a['I' - 'A']; --a['G' - 'A']; --a['H' - 'A']; --a['T' - 'A'];
           break;
        case 9:
           a['N'-'A']-=2; --a['I' - 'A']; --a['E' - 'A'];
           break;
        
    }
}
void increment(int a[], int n)
{
    switch(n) {
        case 0:
           ++a['Z'-'A']; ++a['E' - 'A']; ++a['R' - 'A']; ++a['O' - 'A'];
           break;
        case 1:
           ++a['O'-'A']; ++a['N' - 'A']; ++a['E' - 'A'];
           break;
        case 2:
           ++a['T'-'A']; ++a['W' - 'A']; ++a['O' - 'A'];
           break;
        case 3:
           ++a['T'-'A']; ++a['H' - 'A']; ++a['R' - 'A']; a['E' - 'A']+=2;
           break;
        case 4:
           ++a['F'-'A']; ++a['O' - 'A']; ++a['U' - 'A']; ++a['R' - 'A'];
           break;
        case 5:
           ++a['F'-'A']; ++a['I' - 'A']; ++a['V' - 'A']; ++a['E' - 'A'];
           break;
        case 6:
           ++a['S'-'A']; ++a['I' - 'A']; ++a['X' - 'A'];
           break;
        case 7:
           ++a['S'-'A']; a['E' - 'A']+=2; ++a['V' - 'A']; ++a['N' - 'A'];
           break;
        case 8:
           ++a['E'-'A']; ++a['I' - 'A']; ++a['G' - 'A']; ++a['H' - 'A']; ++a['T' - 'A'];
           break;
        case 9:
           a['N'-'A']+=2; ++a['I' - 'A']; ++a['E' - 'A'];
           break;
        
    }
}
bool isDone(int cnt[])
{
  for(int i=0; i<26; i++)
  {
     if(cnt[i] > 0)
       return false;
  }
  return true;
}

bool fun(int cnt[], int cd[])
{
  if(isDone(cnt))
   return true;
  for(int j=0; j<10; j++) {
    if(has(cnt, j)) {
      decrement(cnt, j);
      cd[j]++;
     if(fun(cnt, cd))
      return true;
      increment(cnt, j);
      cd[j]--;
   }
  }
  return false;
}

int main()
{
	int T;
	cin>>T;
	for(int t=1; t<=T; t++) {
		string str;
		cin>>str;
                int cnt[26] = {0};
                int i = 0;
		while(str[i] != '\0') {
                    cnt[str[i] - 'A']++;
                    i++;
		}
                int cd[10] = {0};
                fun(cnt, cd);
	cout<<"Case #"<<t<<": ";
                for(int k=0; k<10; k++) {
                    while(cd[k]>0) {
                        cout<<k;
                        cd[k]--;
                    }
                }
	cout<<endl;
	}
}

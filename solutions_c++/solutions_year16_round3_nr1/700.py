#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
int t;
scanf("%d", &t);
for(int c=1;c<=t;c++){
 int p;
 scanf("%d",&p);
 vector<int> s;
 int tmp;
 int tot=0;
 for(int i=0;i<p;i++){scanf("%d",&tmp);s.push_back(tmp);tot+=tmp;}
 printf("Case #%d: ",c);
 while(tot>2){
 if(p==2){tot-=2; printf("AB ");continue;} 
 auto m = max_element(s.begin(),s.end());
// if(*m > tot/2) printf("WAT\n");
 int i =(m-s.begin());
 printf("%c ", i+'A' );
 s[i]--;
 tot--;
 }
 auto m1 = max_element(s.begin(),s.end());
 int i =(m1-s.begin());
 s[i]=0;
 auto m2 = max_element(s.begin(),s.end());
 printf("%c%c\n", (m1-s.begin())+'A',(m2-s.begin())+'A' );
 
}
return 0;
}

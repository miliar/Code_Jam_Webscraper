#include <iostream>

using namespace std;

int main(){
 char p[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

 int c; cin >> c;
 for(int a=0;a<c;a++) {
  cout << "Case #" << a+1 << ": ";

 int n; cin >> n;
 int l[26];
 int mem=0;
 for(int i=0;i<n;i++){
  int x; cin >> x;
  l[i] = x;
  mem+=x;
 }

 while(mem>0){
  int bigteam1=-1, bigteam2=-1;
  for(int i=0;i<n;i++)
   if(bigteam1==-1 || l[bigteam1]<l[i]) bigteam1=i;
if((double)l[bigteam1]/mem > 0.5 && mem > 1) cout << l[bigteam1] << " " << mem << " " << (double)l[bigteam1]/mem << endl;
  l[bigteam1]--;

  if(mem%2==0){
   for(int i=0;i<n;i++)
    if(bigteam2==-1 || l[bigteam2]<l[i]) bigteam2=i;
   l[bigteam2]--;
   mem--;
  }
  mem--;

  cout << p[bigteam1];
  if(bigteam2>-1) cout << p[bigteam2];
  if(mem) cout << " ";
 }
 cout << endl;

 }
 return 0;
}
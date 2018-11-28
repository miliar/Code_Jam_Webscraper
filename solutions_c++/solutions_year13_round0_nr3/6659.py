#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;
int T,lower,upper,n=0,ls,us,al,au;
void fs(int l, int u);
bool ips(int m);
bool pal(int pn);
char* i2s(int number);
ifstream fin("C-small-attempt3.in");
ofstream fout("output3.txt");
int main()
{
    fin>>T;
    for(int i=0;i<T;i++){
        n=0;
    fin>>lower;fin>>upper;
    fout<<"Case "<<"#"<<i+1<<": ";

     fs(lower,upper);
     fout<<" "<<n<<endl;
    }

    return 0;
    system("pause");
}

void fs(int l, int u){
al=0;au=0;
for(int s=l;s<=u;s++){
if(ips(s)&&pal(s)){
    cout<<"s:"<<s<<" ";
    al=sqrt(s);break;
    }
}
for(int r=u;r>=l;r--){
if(ips(r)&&pal(r)){
    cout<<"r:"<<r<<endl;
    au=sqrt(r);break;
    }
}
cout<<"al: "<<al<<" au: "<<au<<endl;

for(int k=al;k<=au;k++){
if(ips(k*k)&&pal(k)&&pal(k*k)){
    n++;cout<<k*k<<" is fair n square"<<endl;
}
}
}

bool ips(int m) {
    int root(round(sqrt(m)));
    return (m == root * root);
}

bool pal(int pn){
if(pn==0)return false;
else if(pn<10)return true;
else if((pn%10)==0)return false;
else{
string no,rno;
no=i2s(pn);
for(int i=no.size()-1;i>=0;i--)
rno+=no[i];
return (rno==no);
}
}

char* i2s(int number) {
  char* newString;
  int rem;
  int nod = (log10(number)) + 1;
  newString = new char[nod + 1];  newString[nod] = '\0';
  for (int i = nod-1; i >= 0; --i) {
    int remainder = number % 10;
    char rem_char = (char)(remainder + '0');
    newString[i] = rem_char;
    number = number / 10;
  }
  return newString;
}

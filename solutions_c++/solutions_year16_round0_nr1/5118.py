#include<stdio.h>
#include<iostream>
#include<fstream>

using namespace std;

int check(int a[]){int k=0;
for(int i=0;i<10;i++)k+=a[i];
return k;
}

int answer(int x){
int result =x;
int tmp=1;
char a[600000];
int b[10]={1,1,1,1,1,1,1,1,1,1};
while(check(b)){
  itoa(result,a,10);
  tmp=strlen(a);
  for(int i=0;i<tmp;i++){
    if(b[a[i]-48]!=0)b[a[i]-48]=0;
  }
  result+=x;
  }
return result-x;
}


 int main() {
  /* code */
  int caseNum;
  int* num;
  freopen("A-large.in","r",stdin);
  freopen("out.txt","w",stdout);
  cin>>caseNum;
  num= new int[caseNum];
  for(int i=0;i<caseNum;i++){
	  cin>>num[i];
  }
  for(int i=0;i<caseNum;i++){
	  if(num[i]==0)  cout<<" Case #"<<i+1<<": INSOMNIA"<<endl;
    else{
		cout<<" Case #"<<i+1<<": "<<answer(num[i])<<"\n";
	}
  }
  return 0;

}

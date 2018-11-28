#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main(){
  int n;
  cin >> n;
  for(int cnt=0;cnt<n;cnt++){//実行回数
    double C,F,X;
    double answer=100000;
    cin >>C>>F>>X;
    double per = 2;
    double sec=0;
    
    for(int i=0;i<10000;i++){
      
      for(int j=0;j<i;j++){
	sec += C/per;
	per+=F;
	//printf("sec=%.7f,per=%f\n",sec,per);
      }
      sec += X/per;
      if(sec<answer){answer=sec;//cout<<"small!";
      }

      sec=0;
      per=2;
    }
    cout << "Case #" << cnt+1 << ": " ;
    printf("%.7f",answer);

    cout << endl;
  }
}

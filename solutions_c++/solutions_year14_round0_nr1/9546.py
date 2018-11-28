#include<iostream>
#include<string>
using namespace std;

int main(){
  int n;
  cin >> n;
  for(int cnt=0;cnt<n;cnt++){//実行回数
    int ans1,ans2;
    cin >> ans1;
    int onelines[4][4];
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	cin >> onelines[i][j];
      }
    }
    cin >> ans2;
    int twolines[4][4];
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	cin >> twolines[i][j];
      }
    }

    int num=0;
    int answer;

    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	if(onelines[ans1-1][i]==twolines[ans2-1][j]){
	  num++;answer=onelines[ans1-1][i];}
      }
    }


    cout << "Case #" << cnt+1 << ": " ;

    if(num==0){cout << "Volunteer cheated!";
    }else if(num==1){cout << answer;
    }else{cout << "Bad magician!";}

    cout << endl;
  }
}

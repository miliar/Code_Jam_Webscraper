#include<iostream>
#include<math.h>

using namespace std;


int main(){
  int T;

  cin>>T;
  
  for(int i = 0;i < T;i++){
    int caseNo = i+1;
    int firstAns;
    cin >> firstAns;
    
    //      cout <<"first:"<<firstAns<<endl;
    int lines[4];
    
    for(int j=0;j<4;j++){
      lines[j] = 0;
      for(int k=0;k<4;k++){
	int v;
	cin >> v;
	//	cout <<v<<" ";
	int shifted = 1<<(v-1);
	lines[j] |= shifted; 
	
      }
      //   cout <<endl;
    }
    int secondAns;
    cin >> secondAns;
    // cout <<"second:"<<secondAns<<endl;

    int secondLines[4];
    
    for(int j=0;j<4;j++){
      secondLines[j] = 0;
      for(int k=0;k<4;k++){
	int v;
	cin >> v;
	//	cout << v <<" ";
	int shifted = 1<<(v-1);
	secondLines[j] |= shifted; 
      }
      //        cout <<endl;
    }

    
    int diff = lines[firstAns-1] & secondLines[secondAns -1 ];

    //    cout << "diff:"<<diff<<endl;
    cout << "Case #"<<caseNo<<": ";
    
    if (diff == 0){
      cout << "Volunteer cheated!";
    }
    else if((diff & (diff-1))==0){
     
       for (int j = 0;j<=16;j++){

	 if(diff == (1<<j)){
	   cout <<j+1;
	   break;
	 }
       }
 
    } else {
      cout << "Bad magician!"; 
    }
    cout <<endl;
  }

  return 0;
}

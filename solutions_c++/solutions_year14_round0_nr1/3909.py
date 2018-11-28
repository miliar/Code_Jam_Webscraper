#include <iostream>
using namespace std;

bool nums[16];

int main(int argc, char **argv) {
    int T, ans, i, j, aux1, aux2, aux3, aux4, count;
    cin>>T;
    for(i=1; i<=T; i++) {
      for(j=0; j<16; j++)
	nums[j]=true;
      
      cin>>ans;
      for(j=1; j<5; j++) {
	cin>>aux1>>aux2>>aux3>>aux4;
	if(ans!=j) {
	  nums[aux1-1]=false;
	  nums[aux2-1]=false;
	  nums[aux3-1]=false;
	  nums[aux4-1]=false;
	}
      }
      
            cin>>ans;
      for(j=1; j<5; j++) {
	cin>>aux1>>aux2>>aux3>>aux4;
	if(ans!=j) {
	  nums[aux1-1]=false;
	  nums[aux2-1]=false;
	  nums[aux3-1]=false;
	  nums[aux4-1]=false;
	}
      }
      
      count=0;
      for(j=0; j<16;j++) {
	if(nums[j]) {
	  count++;
	  aux1=j+1;
	}
      }
      if(count==1)
	cout<<"Case #"<<i<<": "<<aux1<<endl;
      else if(count==0)
	cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
      else
	cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
    }
    return 0;
}

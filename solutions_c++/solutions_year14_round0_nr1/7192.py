#include<iostream>
#include<cstdio>
using namespace std;

int main() {
	//  freopen("A-small-attempt1.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
	int t,c=0,k,r=1;
	int r1,r2;
	int arr[4][4];
	int arr1[4],arr2[4];
	cin>>t;
	while(t--) {
		c=0;
		//input first ans
		cin>>r1;
		//entering the cards first time
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>arr[i][j];
			}
		}
		//storing that row
		for(int i=r1-1;i<r1;i++) {
			for(int j=0;j<4;j++) {
				arr1[j]=arr[i][j];
			}
		}
		//input second ans
		cin>>r2;
		//entering the cards second time
			for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>arr[i][j];
			}
		}
		//storing second time 
		for(int i=r2-1;i<r2;i++) {
			for(int j=0;j<4;j++) {
				arr2[j]=arr[i][j];
			}
		}
		//finally the solution
		for(int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				if(arr1[i]==arr2[j])
				{c++;
				k=arr1[i];}
			}
			
		}
		if(c==0)
		cout<<"Case #"<<r<<": Volunteer cheated!"<<"\n";
		else if(c==1)
		cout<<"Case #"<<r<<": "<<k<<"\n";
		else 
		cout<<"Case #"<<r<<": Bad magician!"<<"\n";
		r++;
		 
	}
}

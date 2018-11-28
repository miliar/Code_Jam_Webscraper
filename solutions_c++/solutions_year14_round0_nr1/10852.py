#include <iostream>

using namespace std;

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	cin>>t;
	int index=1;
	while(t--) {
		int n1,n2,temp;
		cin>>n1;
		int arr[4];
		int arr2[4];
		for(int i=0;i<4;i++)
			{
				if(i==n1-1) 
					cin>>arr[0]>>arr[1]>>arr[2]>>arr[3];
				else	cin>>temp>>temp>>temp>>temp;
			}
		cin>>n2;
		for(int i=0;i<4;i++)
			{
				if(i==n2-1) 
					cin>>arr2[0]>>arr2[1]>>arr2[2]>>arr2[3];
				else	cin>>temp>>temp>>temp>>temp;
			}
		int count=0,val;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++) {
				if(arr[i]==arr2[j])	{count++;val=arr[i];}
			}
		if(count==0)
			cout<<"Case #"<<index<<": Volunteer cheated!\n";
		else if(count==1)
			cout<<"Case #"<<index<<": "<<val<<endl;
		else
			cout<<"Case #"<<index<<": Bad magician!\n";
		index++;
	}
	return 0;
}
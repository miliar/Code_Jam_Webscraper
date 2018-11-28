#include<bits/stdc++.h>
using namespace std;
int main()
{
	//freopen("output.txt","w+",stdout);
	//freopen("input.txt","r+",stdin);
	int t;
	
	cin>>t;
	//cout<<t<<endl;
	for(int tt=1;tt<=t;tt++)
	{
	 int arr[4];
	 int arr2[4];
     int f;
	 cin>>f;
	 //scanf("%d",&f);
	 int a,b,c,d,m,n,o,p;
	 for(int i=1;i<=4;i++)
	 {
	 	cin>>a>>b>>c>>d;
	 	//scanf("%d%d%d%d",&a,&b,&c,&d);
	 	if(i==f)
	 	 {
	 	 	m=a,n=b,o=c,p=d;
	 	 }
	 }
	 int l;
	 //scanf("%d",&l);
	 cin>>l;
	 int q,r,s,u;
	 for(int i=1;i<=4;i++)
	 {
	 	cin>>a>>b>>c>>d;
	 	//scanf("%d%d%d%d",&a,&b,&c,&d);
	 	if(i==l)
	 	{
	 		q=a,r=b,s=c,u=d;
	 	}
	 }
	 int same=0;
	 int index;
	 arr[0]=q,arr[1]=r,arr[2]=s,arr[3]=u;
	 arr2[0]=m,arr2[1]=n,arr2[2]=o,arr2[3]=p;
	 sort(arr,arr+4);
	 sort(arr2,arr2+4);
	 for(int i=0;i<4;i++)
	 {
	 	for(int j=0;j<4;j++)
	 	{
	 		if(arr[i]==arr2[j])
	 		{
	 			same++;
	 			index= arr[i];
	 		}
	 	}
	 }
	 if(same==1)
	 {
	 	cout<<"Case #"<<tt<<": "<<index<<endl;
	 }
	 else if(same>1 && same<=4)
	 {
	 	cout<<"Case #"<<tt<<": "<<"Bad magician!"<<endl;
	 }
	 else if(same==0)
	 {
	 	cout<<"Case #"<<tt<<": "<<"Volunteer cheated!"<<endl;
	 }
	
	  	
	}
}

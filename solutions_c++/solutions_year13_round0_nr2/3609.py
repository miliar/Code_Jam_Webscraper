#include<iostream>
#include<string.h>

using namespace std;

int rmax[103]={0},cmax[103]={0},rmin[103]={0}, cmin[103]={0},a[103][103]={0},b[103][103]={0};

//check if b[][] = a[][]
 bool check(int m,int n)
{
	int i,j;
	for(i=1;i<=m;i++)
	 for(j=1;j<=n;j++) {
	//	cout<<i<<" "<<j<<" -> "<<a[i][j]<<" "<<b[i][j]<<endl;
		if(a[i][j]!=b[i][j])
			return false;
	 }
		return true;
}

int fun(int m,int n,int r)
{
	int i,j;
	 for(j=1;j<=n;j++) {
		if(a[r][j]!=b[r][j])
			return j;
	 }
		return 0;
}

int main()
{

	int i,j,k,n,c,m,t,dot,x,z,ans,f=0;
	
	cin>>t;
	
	for(k=1;k<=t;k++) {
		for(i=0;i<=102;i++)for(j=0;j<=102;j++) { cmax[i]=0; rmax[i]=0; cmin[i]=0; rmin[i]=0; a[i][j]=0;b[i][j]=0;}
		f=0;ans=0;
		cin>>m>>n;
		
		//cout<<k<<" "<<m<<" "<<n<<endl;
		
		for(i=1;i<=m;i++) {
			for(j=1;j<=n;j++) {
				cin>>a[i][j];
				//Row maximum
				if(a[i][j]>rmax[i])
					rmax[i] = a[i][j];
				}
			}
		if(m==1 || n==1) {
		cout<<"Case #"<<k<<": YES"<<endl; 
		continue;
		}
			
		//Column Maximum
    	for(i=1;i<=n;i++)
			for(j=1;j<=m;j++) 
				if(a[j][i]>cmax[i])	cmax[i] = a[j][i];
			
			
		//Assign Row max
		for(i=1;i<=m;i++)
			for(j=1;j<=n;j++) b[i][j] = rmax[i];
			
			
		if(check(m,n)) {cout<<"Case #"<<k<<": YES"<<endl;continue;}
		
			
		for(i=1;i<=m;i++) {
			for(z=1;z<=n;z++) {
			x = fun(m,n,i); // return column number
			
			if(x>0 && cmax[x]>a[i][x]) {cout<<"Case #"<<k<<": NO"<<endl;f=1;break;}
			if(x!=0)
			for(j=1;j<=m;j++) { if(b[j][x]>a[i][x]) b[j][x]=a[i][x]; }
		
			}
			if(f==1) break;
		}
	
		if(check(m,n)) {cout<<"Case #"<<k<<": YES"<<endl;}
		else if(f!=1){cout<<"Case #"<<k<<": NO"<<endl;}
	
		
		
	}
	return 0;
}


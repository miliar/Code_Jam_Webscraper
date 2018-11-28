#include <fstream>
#include <algorithm>
using namespace std;
int main()
{
	ifstream fin("D-large.in");
	ofstream fout("D-small-attempt0.out");
	 int t,tt,n;
	 fin>>t;
	 tt=t;
	 float a[1001],b[1001];
	 while(t)
	 {
	 fin>>n;
	 int flag[1001];
	 
	 	int i,j,ans1=0,ans=0;
	 	 ans1=0;
	 	for (i=0;i<n;i++)
	 	flag[i]=0;
	 	 for (i=0;i<n;i++)fin>>a[i];
	 	 for (i=0;i<n;i++)fin>>b[i];
	 	 sort(a,a+n);
	 	 sort(b,b+n);
	 	i=n-1;
	 	 while(i>=0)
	 	{
	 		j=n-1;
	 		while (j>=0&&b[j]>a[i])
	 	  	j--;
	 	  	j++;
	 	  	while (flag[j]&&j<n)j++;
	 	 if (j>=0&&j!=n) {++ans1;flag[j]=1;}
	 	 i--;
		 }
		 ans1=n-ans1;
		
		 ans=0;
	
	int	k=0;
  i=0; int ii=n-1; j=0; int jj=n-1;
  for (k=0;k<n;k++)
    {
      if (a[ii]<b[jj])   
        {
          ++i;    --jj;
         continue;
        }
      if (a[ii]>b[jj])   
        {
          --ii; --jj;
          ans++; continue;
        }
      if (a[i]<b[j])   
        {
          ++i; --jj;
         continue;
        }
      if (a[i]>b[j])   
        {
          ++i; ++j;
          ans++; continue;
        }
      if ((a[ii]=b[jj])&&(a[i]=b[j]))   
        {
          if (a[i]=b[jj])   ans=ans;
            else if (a[i]<b[jj])    ans=ans;
              else if (a[i]>b[jj])    ans++;
          ++i; --jj;
        }
    }
	 fout<<"Case #"<<tt-t+1<<": "<<ans<<' '<<ans1<<endl;
	 t--;
 }
 fin.close();
 fout.close();
 return 0;
}

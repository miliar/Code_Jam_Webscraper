#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C-small-attempt0.in");
	fout.open("C-small-attempt0.out");
    int t,j,i,k,c,z,count=0,q,qq;
    bool flag,flagb;
    long long int num,x;
    //printf("after\n");
    int a[16]={1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};
    int ans[12];
    fin>>t;
    fout<<"Case #1:"<<endl;
    while(t--)
    {
		fin>>q>>qq;
		//printf("in while\n");
        for(i=0;i<=16384;i++)
        {
            flag=false;
            for(k=2;k<=10;k++)
            {
				flagb=false;
				//printf("in for\n");
                num=0;
                for(z=15;z>=0;z--)
                {
                    if(a[z]==1)
                    {
						x=pow(k,15-z);
						num+=x;
					}
                }
                //printf("i=%d k=%d num=%lld\n",i,k,num);
                //printf("in\n");
                for(x=2;x<sqrt(num);x++)
                {
                    if(num%x==0)
                    {
						flagb=true;
                        if(k==10)
                        flag=true;
                        ans[k]=x;
                        break;
                    }
                }
				if(flagb==false)
				break;
            }
            if(flag==true)
            {
				for(x=0;x<16;x++)
				fout<<a[x];
				//printf("%d",a[x]);
				fout<<" ";
				//printf(" ");
				for(x=2;x<=10;x++)
				fout<<ans[x]<<" ";
				//printf("%d ",ans[x]);
				fout<<"\n";
				//printf("\n");
				count++;
				if(count==50)
				return 0;
			}
            c=1;
            for(j=14;j>0;j--)
            {
                a[j]+=c;
                c=a[j]/2;
                a[j]%=2;
            }
        }
    }
    fin.close();
    fout.close();
    return 0;
}

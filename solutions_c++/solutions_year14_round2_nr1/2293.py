#include<bits/stdc++.h>
using namespace std;
int diff(int a,int b)
{
    if(a<b) return (b-a);
    else return (a-b);
}
int main()
{

    int t,n,j,i,k,u,no;
    char str[104];
    scanf("%d",&t);
    for(no=0;no<t;no++)
    {
    	printf("Case #%d: ",no+1);
        int best=0;
        int a[104][104][2]={0};
        int maxe=0;
        scanf("%d",&n);
        for(u=0;u<n;u++)
        {
            scanf("%s",str);
            i=0;
            j=0;

            while(str[i]!='\0')
            {
                if(str[i]==str[i+1])
                {
                    a[u][j][0]=str[i];
                    a[u][j][1]=a[u][j][1]+1;
                }
                else {a[u][j][0]=str[i]; a[u][j][1]=a[u][j][1]+1; j++;}
                i++;
            }

            /*for(k=0;k<j;k++)
            {
                printf("%c %d\n",a[u][k][0],a[u][k][1]);
            }*/
            if(j>maxe) maxe=j;
        }
        int check=0;
        for(j=0;j<maxe;j++)
        {
            u=a[0][j][0];
            i=0;
            while(i<n)
            {
                if(a[i][j][1]>best) best=a[i][j][1];
                if(a[i][j][0]==u) i++;
                else {check=1; break;}
            }
            if(check==1) break;
        }
        if(check==1) {printf("Fegla Won\n"); continue;}

        int mini=12345667,z=0;
        int meane=0;
      for(k=0;k<maxe;k++)
      {
          float mean=0;
          for(i=0;i<n;i++) mean=mean+a[i][k][1];
          mean=mean/n;

          if(mean>(int)mean+0.5) meane=(int)mean+1;
          else meane=(int)mean;
		//	printf("che %d\n",meane);

          for(i=0;i<n;i++) z=z+diff(a[i][k][1],meane);

      }
      printf("%d\n",z);


    }
    return 0;
}

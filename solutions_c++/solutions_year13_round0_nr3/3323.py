#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int aSize=9,j,cSize=0,bSize=9,aS=1,bS=2,d[1000];
char a[100][16],b[100][16],c[1000][16],check1[16];
int main()
{
    freopen ("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int current=2,Size=3,check;
    for(int i=1;i<=aSize;i++)
    {
            c[i][0]=a[i][0]=char(i+48);
            c[i][1]=a[i][1]='\0';        
    }
    cSize+=aSize;
    for(int i=1;i<=bSize;i++)
    {
            c[i+cSize][0]=a[i][0]=char(i+48);
            c[i+cSize][1]=a[i][1]=char(i+48);
            c[i+cSize][2]=a[i][2]='\0';         
    }
    cSize+=bSize;
    //for(int i=1;i<=cSize;i++)
      //      printf("%s \n",c[i]);
    
    int count=cSize;
    cSize++;
    while(current!=Size)
    {
                        for(int i=1;i<count;i++)
                        {
                                check=atoi(c[i]);
                                check=check*check;
                                itoa(check,check1,10);
                                check=strlen(check1);
                                if(check==3)
                                {
                                            c[cSize][0]=check1[0];
                                            c[cSize][1]=check1[1];
                                            c[cSize][2]=check1[2];
                                            c[cSize][3]='\0';
                                            cSize++;
                                }
                                else if(check>3)
                                {
                                     current++;
                                     break;
                                }
                                
                        }                       
    }
    
    float one;
    int two,t=0,s;
    //Checking Fair And Square Number
    for(int i=1;i<cSize;i++)
    {
            check=atoi(c[i]);
            one=sqrt(check);
            two=(int)one;
            if(one==two)
                        d[t++]=check;
    }
    
    int t1,low,high,q;
    scanf("%d",&t1);
    count=0,q=0;
    while(t1--)
    {
        count=0;
        scanf("%d %d",&low,&high);   
        for(int i=0;i<t;i++)
        {
                if(d[i]<low)
                            continue;
                if(d[i]>high)
                             break;
                else
                    count++;
        }
        printf("Case #%d: %d\n",q++,count);         
    }
    
    
    getchar();
    return 0;
}

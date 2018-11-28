#include<iostream>
#include<cstdlib>
#include<cmath>
using namespace std;
bool isPelindrome(int);
char *toString(int);
int main()
{
    int T;
    scanf("%d",&T);
    int i,j;
    int A,B;
    int count=0;
    double d;
    bool perfect_square;
    for(i=0;i<T;i++)
    {
        scanf("%d%d",&A,&B);
        for(j=A;j<=B;j++)
        {
            perfect_square=false;
            d=(double)j;
            if( (sqrt(d)-(int)sqrt(j))==0 )
            {
                perfect_square=true;
                //cout<<"PS: "<<j<<endl;;
            }
            if(perfect_square && isPelindrome(j) && isPelindrome(sqrt(j)))
            {
             //   cout<<"num : " << j <<endl;
                count++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
        count=0;
    }
    return 0;
}
bool isPelindrome(int num)
{
    char str1[100];
    char str2[100];
    strcpy(str1,toString(num));
    strcpy(str2,strrev(toString(num)));
    if(strcmp(str1,str2)==0)
        return true;
    return false;
}
char * toString(int num)
{
    char str[100];
    int i=0;
    while(num!=0)
    {
        str[i++]=num%10+'0';
        num=num/10;
    }
    str[i]='\0';
    return str;
}

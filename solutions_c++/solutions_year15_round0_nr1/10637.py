
#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int t,a,ans,people,i,n,j;
    char ch,s[1001],zero='0';
    FILE * input_values;
    input_values = fopen("A-small-attempt1.in","r");
    ch = fscanf(input_values, "%d",&t);
ofstream myfile;
  myfile.open ("output.out");
  //myfile << "Writing this to a file.\n";
  //myfile.close();
while(ch != EOF)
{

    //scanf("%d",&t);
    a=t;
    while(t--)
    {
        ch = fscanf(input_values, "%d %s",&n,s);
        //scanf("%d %s",&n,s);
        ans=0;
        j=0;
        people=0;
        if(s[0]==zero)
            {
                ans+=1;
                people+=1;
                j=0;
            }
        else
            {
                people+=s[0]-zero;
            }
        for(i=1;i<=n;i++)
        {

            if(s[i]==zero)
                j++;
            if(people < i && s[i]!=zero)
                {
                    ans+= i - people;
                    people+=(i - people);
                }
            people+= (s[i] - zero);
        }
        if(j>n)
            ans=0;
        //printf("Case #%d: %d\n",a-t,ans);
        myfile<<"Case #"<<(a-t)<<": "<<ans<<endl;
    }
    ch = fscanf(input_values, "%d",&t);
}
myfile.close();

    return 0;
}

//A-small-attempt0.in

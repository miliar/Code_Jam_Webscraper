#include<set>
#include<stdio.h>

using namespace std;
set<int>s;

int main()
{
    int t,counter=1,number;
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	scanf("%d",&t);
    while(t--)
    {
        bool flag=0;

        scanf("%d",&number);
        s.clear();

        printf("Case #%d: ",counter++);

        int counter2=1;

        if(number==0)
            printf("INSOMNIA\n");

        else
        {
            while(1)
            {
                int take2=number*counter2;
                int save=take2;
                //cout<<"take2= "<<take2<<endl;



                while(take2!=0)
                {
                    int take=take2%10;
                    //cout<<"last digit= "<<take<<endl;
                    take2=take2/10;
                    s.insert(take);
					//cout<<"set size= "<<s.size()<<endl;
                    if(s.size()==10)
                    {
                        printf("%d\n",save);
                        flag=1;
                        break;
                    }
                }
                //cout<<"run\n";
                if(flag)
                    break;
				counter2++;
            }
        }


    }
    return 0;
}

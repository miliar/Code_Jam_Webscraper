#include<iostream>
#include<string>


using namespace std;

int digs_freq[10][2];
void incr_count(int a)
{
    digs_freq[a][1]++;
}

 int length(int a)
{
    int x=a;
    int l=0;
    while(x!=0)
    {
        x=x/10;
        l++;
    }

    return l;

}

int getFlag(int a[][2])
{

    int flag=0;
    for(int i=0;i<10;i++)
    {
        if(digs_freq[i][1]>0)
        {
           flag=1;

        }
        else
        {

            flag=0;
            break;
        }
    }

    return flag;

}
int main()
{


    for(int i=0;i<10;i++)
    {
        digs_freq[i][0]=i;
        digs_freq[i][1]=0;

    }


		int t=0;
        int n=0;
        int q=1;
        int ass=1;
        cin>>t;
		while(t!=0)
		{


		   for(int i=0;i<10;i++)
            {
                digs_freq[i][0]=i;
                digs_freq[i][1]=0;

            }


		    t--;
             q=1;
			 n=0;
			cin>>n;
			int temp=n,tem=n,f=0;
			while(true)
			{


                    if(n==0)
                    {

                        cout<<"Case #"<<ass<<": INSOMNIA"<<endl;
                        ass++;
                        break;

                    }
                    else{
                    while(length(temp)!=0)
                    {


                          f=temp%10;
                          temp=temp/10;
                          incr_count(f);



                    }


                       q++;
                    temp=tem;
                    temp=n*q;
                    tem=n*q;

                if(getFlag(digs_freq)==1)
                {


                    cout<<"Case #"<<ass<<":"<<" "<<n*(q-1)<<endl;
                    ass++;
                    break;
                }






			}


			}


		}




	}


#include <iostream>
using namespace std;
int main(void)
{
        long t,i,f,r,j,x,k,n;
        long a[10];
            x=1;

            cin>>t;

        while(x<=t)
            {

                       		f=0;

                              for(i=0;i<10;i++)
                                {

                                    a[i]=i;

                                }

                            cin>>n;

                       		if(n==0)
                                {

                       			cout<<"Case #"<<x<<": INSOMNIA\n";


                        		}

                        else
                        {

                            for(i=1;i<=1000000;i++)
                            {

                        			k=i*n;

                                    while(k != 0)
                                    {
                                        r = k % 10;

                       				for(j=0;j<=9;j++)
                                        {
                                            if(r==a[j])
                                            {

                                                f++;

                        						a[j]=10;
                        						break;

                        					}

                        				}

                                    k = k / 10;

                        			}

                        			if(f==10)
                                    {
                       				cout<<"Case #"<<x<<": "<<i*n<<"\n";
                                    break;
                                    }

                            }

                        }
                     		x++;
                }

    return 0;
        }


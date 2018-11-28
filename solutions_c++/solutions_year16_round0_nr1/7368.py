#include <iostream>
#include <fstream>

using namespace std;
int A[10]={0,0,0,0,0,0,0,0,0,0};
bool checkArr ()
{
    int i=0;
    bool flag = true;
    for(i=0;i<10;i++)
    {
        if(!A[i])
        {
            flag=false;
        }
    }
    cout<<"Check Array\n";
    return flag;
}

void reloadArr()
{
    int i=0;
    for(i=0;i<10;i++)
        A[i]=0;
        cout<<"Reload Array\n";
}

int main()
{
    ifstream input;
    ofstream output;
     input.open("A-large.in");
     output.open("output_LARGE.txt");
     int N,num,i=0,sum,mymod,mydiv;
        bool flag=true;
   // if (input.is_open())
    {
        input >> N;
        for (i=0;i<N;i++)
        {
            output<<"Case #"<<i+1<<": ";
            input >> num;
            sum=num;
                if (sum)
                {

                do{
                    cout<<"Outer Do\n";
                    mydiv=sum;

                    while(mydiv)
                        {

                        mymod=mydiv%10;
                        mydiv=mydiv/10;
                        A[mymod]=1;
                        }
                    sum+=num;


                    flag=checkArr();
                }while(!flag);

                reloadArr();
                }
                if(sum)
                    output<<sum-num<<endl;
                else
                    output<<"INSOMNIA"<<endl;
        }

    }

    input.close();
    output.close();
    return 0;
}

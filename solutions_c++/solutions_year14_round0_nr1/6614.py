#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int testCases,ans1,ans2,A[4],B[4],temp,count=0,flag,ans;
    ifstream myfileInput;
    ofstream myfileOutput;
    myfileInput.open("input.txt");
    myfileOutput.open("output.txt");
    myfileInput>>testCases;
    while(testCases>0)
    {
        flag=0;
        myfileInput>>ans1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(i==ans1-1)
                {
                        myfileInput>>A[j];
                }
                else
                {
                    myfileInput>>temp;
                }
            }
        }
        myfileInput>>ans2;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(i==ans2-1)
                {
                        myfileInput>>B[j];
                }
                else
                {
                    myfileInput>>temp;
                }
            }
        }
        count++;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(A[i]==B[j])
                {
                    flag++;
                    ans=A[i];
                }
            }
        }
        if(flag==0)
        {
            myfileOutput<<"Case #"<<count<<": Volunteer cheated!\n";
        }
        else if(flag==1)
        {
            myfileOutput<<"Case #"<<count<<": "<<ans<<"\n";
        }
        else
        {
            myfileOutput<<"Case #"<<count<<": Bad magician!\n";
        }
        testCases--;
    }
    myfileInput.close();
    myfileOutput.close();

}


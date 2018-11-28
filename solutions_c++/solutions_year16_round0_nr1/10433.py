#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

void Count(int Max,int input,int n)
{
    bool ans0=false,ans1=false,ans2=false,ans3=false,ans4=false,ans5=false,ans6=false,ans7=false,ans8=false,ans9=false;
    int num=0,x=0,i=1,ans=0,solution[101];
    while((!ans0)||(!ans1)||(!ans2)||(!ans3)||(!ans4)||(!ans5)||(!ans6)||(!ans7)||(!ans8)||(!ans9))
    {
        if(input<=0)
            break;
        num = i*input;
        ans = num;
        while(1)
        {
            x = num%10;
            num = num/10;
            if(x==0)
                ans0 = true;
            if(x==1)
                ans1 = true;
            if(x==2)
                ans2 = true;
            if(x==3)
                ans3 = true;
            if(x==4)
                ans4 = true;
            if(x==5)
                ans5 = true;
            if(x==6)
                ans6 = true;
            if(x==7)
                ans7 = true;
            if(x==8)
                ans8 = true;
            if(x==9)
                ans9 = true;
            if(num==0)
                break;
        }
        i++;
    }
    solution[n] = ans;
    //cout << solution[n];
    ofstream outfile;
    outfile.open("AL.out");
    for(int i=1; i<=Max; i++)
    {
        if(solution[i]<=0)
        {
            outfile << "Case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            outfile << "Case #" << i << ": " << solution[i] << endl;
        }
    }
    if(input<=0)
    {
        cout << "Case #" << n << ": INSOMNIA" << endl;
    }
    else
    {
        cout << "Case #" << n << ": " << ans << endl;
    }
}
int main ()
{
    string line;
    ifstream myfile ("A-large.in");
    int value[101],i=0;
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            istringstream buffer(line);
            buffer >> value[i];
            i++;
        }
        for(int i=0; i<value[0]; i++)
        {
            Count(value[0],value[i+1],i+1);
        }
        myfile.close();
    }
    return 0;
}


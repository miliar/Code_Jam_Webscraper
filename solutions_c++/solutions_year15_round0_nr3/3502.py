#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c_output.txt","w",stdout);
    int NumberOfCases;
    cin>>NumberOfCases;
    int len,numberOfTimes,count;
    string inputStr,workingStr;
    char partI,partJ,partK,calculatedChar;
    for(int caseNo=1;caseNo<=NumberOfCases;caseNo++)
    {
        cin>>len>>numberOfTimes>>inputStr;
        workingStr="";
        count=0;
        for(int i=0;i<numberOfTimes;i++)
        {
            workingStr+=inputStr;
        }
        //cout<<workingStr<<endl;
        calculatedChar = workingStr[0];
        int sign = 1;
        for(int i=1;i<len*numberOfTimes;i++)
        {
            if(count == 0 && calculatedChar == 'i' && sign == 1)
            {
                partI = 'i';
                count++;
                calculatedChar = workingStr[i];
                sign = 1;
                continue;
            }
            else if(count == 1 && calculatedChar == 'j' && sign == 1)
            {
                partJ = 'j';
                count++;
                calculatedChar = workingStr[i];
                sign = 1;
                continue;
            }


            if(calculatedChar == 'i' && workingStr[i] == 'j')
            {
                calculatedChar = 'k';
            }
            else if(calculatedChar == 'i' && workingStr[i] == 'k')
            {
                calculatedChar = 'j';
                sign *= -1;
            }
            else if(calculatedChar == 'j' && workingStr[i] == 'k')
            {
                calculatedChar = 'i';
            }
            else if(calculatedChar == 'j' && workingStr[i] == 'i')
            {
                calculatedChar = 'k';
                sign *= -1;
            }
            else if(calculatedChar == 'k' && workingStr[i] == 'i')
            {
                calculatedChar = 'j';
            }
            else if(calculatedChar == 'k' && workingStr[i] == 'j')
            {
                calculatedChar = 'i';
                sign *= -1;
            }
            else if(calculatedChar == workingStr[i])
            {
                calculatedChar = '1';
                sign *= -1;
            }
            else if(calculatedChar == '1')
            {
                calculatedChar = workingStr[i];
            }
            else
            {
                calculatedChar = '$';
                sign = -1;
                break;
            }

        }
        if(count == 2 && calculatedChar == 'k' && sign == 1)
        {
            partK = 'k';
            count++;
        }
        if(count == 3)
            cout<<"Case #"<<caseNo<<": YES"<<endl;
        else
            cout<<"Case #"<<caseNo<<": NO"<<endl;

    }
}

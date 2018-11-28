#include <iostream>
#include <string>

using namespace std;

int main()
{
    int size;
    int curMax;
    string curText;
    freopen("D:\\ccpptrain\\codejamStand\\A-large.in","r",stdin);
    freopen("D:\\ccpptrain\\codejamStand\\A-largeout.txt","w",stdout);
    cin>>size;
    for(int i=0;i<size;i++)
    {
        cin>>curMax>>curText;
        int tempSum=0;
        int needAdd=0;
        int needAddMax=0;
        int curNum;
        for(int j=0;j<=curMax;j++)
        {
            curNum=curText[j]-'0';
            if(tempSum>=j)
            {
                tempSum+=curNum;
            }
            else
            {
                needAdd=j-tempSum;
                if(needAdd>needAddMax)
                {
                    needAddMax=needAdd;
                }
                tempSum+=curNum;
            }
        }
        cout<<"Case #"<<i+1<<": "<<needAddMax<<endl;
    }

    return 0;

}

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int caseNum,row;
    vector<int> card,subCard,result,output;
    cin>>caseNum;
    for(int k=0;k<caseNum;k++)
    {
        for(int j=0;j<2;j++)
        {
            cin>>row;
            for(int i=0;i<16;++i)
            {
                int temp =0 ;
                cin>>temp;
                card.push_back(temp);
                if(i>=4*(row-1) && i<4*row)
                    subCard.push_back(temp);
            }
        }
        for(int i=0;i<4;i++)
        {
            for(int j=4;j<8;j++)
            {
                if(subCard[i]==subCard[j])
                {
                    result.push_back(subCard[i]);
                    continue;
                }
            }
        }
        if(result.size() == 1)
            output.push_back(result[0]);
        else if(result.size() == 0)
            output.push_back(17);
        else
            output.push_back(18);
        result.clear();
        subCard.clear();
        card.clear();
    }
    for(int k=0;k<caseNum;k++)
    {
        if(output[k] <= 16)
            cout<<"Case #"<<k+1<<": "<<output[k]<<endl;
        else if(output[k] == 17)
            cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
        else
            cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
    }



    return 0;
}

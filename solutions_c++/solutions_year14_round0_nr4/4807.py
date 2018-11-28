#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool compare(double a,double b)
{
    return a>b;
}
int main()
{
    int caseNum;
    vector<int> result1,result2;
    vector<double> naomi,ken;
    cin>>caseNum;
    for(int i=0;i<caseNum;i++)
    {
        int num;
        int score=0;
        cin>>num;

        for(int j=0;j<num;j++)
        {
            double temp;
            cin>>temp;
            naomi.push_back(temp);
        }
        for(int j=0;j<num;j++)
        {
            double temp;
            cin>>temp;
            ken.push_back(temp);
        }
        sort(naomi.begin(),naomi.end(),compare);
        sort(ken.begin(),ken.end(),compare);
        int kenH=0,kenT=num-1;
        for(int k=0;k<num;k++)
        {
            if(naomi[k]>ken[kenH])
            {
                score++;
                kenT--;
            }
            else
            {
                kenH++;
            }
        }
        kenH=0;
        kenT=num-1;
        result2.push_back(score);
        score = 0;

        while(!naomi.empty())
        {
            if(naomi.back()>ken.back())
            {
                score++;
                ken.pop_back();
                naomi.pop_back();
            }
            else
                naomi.pop_back();
        }
        result1.push_back(score);
        naomi.clear();
        ken.clear();

    }
    for(int i=0;i<caseNum;i++)
        cout<<"Case #"<<i+1<<": "<<result1[i]<<' '<<result2[i]<<endl;
    return 0;
}

#include <iostream>
#include <vector>
using namespace std;
int cal(vector<double> data1,vector<double> data2)
{
    int res=0;
    for(unsigned int i=0;i<data1.size();i++)
    {
        for(unsigned int j=i+1;j<data1.size();j++)
        {
            if(data1[i]>data1[j])
            {
                double temp=data1[i];
                data1[i]=data1[j];
                data1[j]=temp;
            }
            if(data2[i]>data2[j])
            {
                double temp=data2[i];
                data2[i]=data2[j];
                data2[j]=temp;
            }
        }
    }


    for(unsigned int h=0;h<data1.size();h++)
    {
        unsigned int m;
        for(m=h;m<data1.size();m++)
        {

            if(data1[m]<data2[m-h])
                break;
        }
        //cout<<temp<<endl;
        if(m==(data1.size()))
        {
            res=data1.size()-h;
            break;
        }

    }
    return res;
}
int main()
{
    unsigned int num;
    cin>>num;
    vector<vector<double>> data;

    for(unsigned int k=0;k<num;k++)
    {
        int sub_num;
        cin>>sub_num;
        vector<double> temp;
        for(int l=0;l<sub_num;l++)
        {
            double input;
            cin>>input;
            temp.push_back(input);
        }
        data.push_back(temp);
        temp.clear();
        for(int l=0;l<sub_num;l++)
        {
            double input;
            cin>>input;
            temp.push_back(input);
        }
        data.push_back(temp);

    }
    for(unsigned int o=0;o<num;o++)
    {
        int a=(data[2*o]).size()-cal(data[2*o+1],data[2*o]);
        int ans=cal(data[2*o],data[2*o+1]);
        cout<<"Case #"<<o+1<<":"<<" "<<ans<<" "<<a<<endl;
    }

    return 0;
}


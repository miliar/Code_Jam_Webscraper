#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int k;
    cin>>k;

    for(int c = 0; c < k; c++)
    {
        int v1[4], v2[4];
        int lugar, ignore;
        cin>>lugar;
        for(int i = 0; i < 4; i++)
        {
            for (int j = 0; j< 4; j++)
            {
                if (i+1 == lugar)
                    cin>>v1[j];
                else
                    cin>>ignore;
            }

        }
        cin>>lugar;
        for(int i = 0; i < 4; i++)
        {
            for (int j = 0; j< 4; j++)
            {
                if (i+1 == lugar)
                    cin>>v2[j];
                else
                    cin>>ignore;
            }

        }
        vector<int> result;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                if(v1[i] == v2[j])
                {

                    result.push_back(v1[i]);
                }
            }
        }
        cout<<"Case #"<<c+1<<": ";
        if (result.size() == 0)
            cout<<"Volunteer cheated!"<<endl;
        else if(result.size() > 1)
            cout<<"Bad magician!"<<endl;
        else
            cout<<result[0]<<endl;
    }
    return 0;
}

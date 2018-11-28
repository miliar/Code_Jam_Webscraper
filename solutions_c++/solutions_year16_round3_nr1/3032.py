#include <bits/stdc++.h>

using namespace std;

bool equalNum(string& ris, vector<int>& num)
{
    if(num[0] == num[1])
    {
        for(int j=0; j<num[2]; j++)
            ris.append("C ");
        for(int j=0; j<num[0]; j++)
            ris.append("AB ");
        return true;
    }
    else if(num[0] == num[2])
    {
        for(int j=0; j<num[1]; j++)
            ris.append("B ");
        for(int j=0; j<num[0]; j++)
            ris.append("AC ");
        return true;
    }
    else if(num[1] == num[2])
    {
        for(int j=0; j<num[0]; j++)
            ris.append("A ");
        for(int j=0; j<num[1]; j++)
            ris.append("BC ");
        return true;
    }
    else
    {
        return false;
    }
}
int giveMeMinor(vector<int>& num)
{
    if(num[0]<num[1] && num[0]<num[2])
        return 0;
    if(num[1]<num[0] && num[1]<num[2])
        return 1;
    else
        return 2;
}
int main(int argc, char** argv)
{
    freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        int n;
        string ris;
        vector<int> num;
        cin >> n;
        for(int j=0; j<n; j++)
        {
            int temp;
            cin >> temp;
            num.push_back(temp);
        }
        switch(n)
        {
            case 2:
                for(int j=0; j<num[0]; j++)
                    ris.append("AB ");

            break;
            case 3:
                while(!equalNum(ris,num))
                {
                    int index = giveMeMinor(num);
                    for(int k=0; k<num.size(); k++)
                    {
                        if(k!=index)
                        {
                            num[k] --;
                            ris.push_back(char(k+65));
                        }
                    }
                    ris.append(" ");
                }
            break;
        }
        cout << "Case #" << i+1 << ": " << ris << endl;
    }
    return 0;
}

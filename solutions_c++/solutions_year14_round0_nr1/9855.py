#include<iostream>
#include<set>
using namespace std;
int N,Case = 0;
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>N;
    while(N--)
    {
		Case++;
        int first, second, arr1[4][4], arr2[4][4];
        set<int> ans;
        cin>>first;
        for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++)
                    cin>>arr1[i][j];
        cin>>second;
        for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++)
                    cin>>arr2[i][j];
        for(int i = 0; i < 4; i++)
            ans.insert(arr1[first-1][i]),ans.insert(arr2[second-1][i]);
        if(ans.size() == 8)
        {
            cout<<"Case #"<<Case<<": Volunteer cheated!"<<endl;
        }
        else if(ans.size() == 7)
        {
            for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                    if(arr1[first-1][i] == arr2[second-1][j])
                        cout<<"Case #"<<Case<<": "<<arr1[first-1][i]<<endl;
				}        
			}

        }
        else
        {
			cout<<"Case #"<<Case<<": Bad magician!"<<endl;
        }
    }
    return 0;
}


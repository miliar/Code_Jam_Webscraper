#include<iostream>
#include <fstream>
using namespace std;
int main()
{
    ofstream myfile("outputs.txt");
    int i;
    cin>>i;

    for(int tc = 1; tc<= i; tc++)
    {

        int arr1[4][4];
        int ans1;
        cin>>ans1;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                cin>>arr1[i][j];
            }
        int arr2[4][4];
        int ans2;
        cin>>ans2;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                cin>>arr2[i][j];
            }
        int counter = 0;
        int ans;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                if(arr1[ans1-1][i] == arr2[ans2-1][j])
                {
                    ans = arr1[ans1-1][i];
                    counter++;
                }
            }
        if(counter == 1)
        {
            myfile<<"Case #"<<tc<<": "<<ans<<endl;
        }
        else if(counter > 1)
        {
            myfile<<"Case #"<<tc<<": Bad magician!"<<endl;
        }
        else
        {
            myfile<<"Case #"<<tc<<": Volunteer cheated!"<<endl;
        }
    }
    return 0;
}

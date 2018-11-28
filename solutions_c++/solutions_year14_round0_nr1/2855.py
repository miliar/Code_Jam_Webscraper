/* 
 * File:   A.cpp
 * Author: metin
 *
 * Created on April 12, 2014, 3:28 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int arr[5][5];
int ans[5];
int ans2[5];
vector<int> sect;
/*
 * 
 */
int main(int argc, char** argv) {
    
    int T, A, temp;
    
    cin >> T;
    for(int i=0; i<T; i++)
    {
        sect.clear();
        cin >> A;
        for(int j=1; j<=4; j++)
        {
            if(j!=A)
                cin>>temp>>temp>>temp>>temp;
            else
                cin>>ans[1]>>ans[2]>>ans[3]>>ans[4];  
        }
        cin >> A;
        for(int j=1; j<=4; j++)
        {
            if(j!=A)
                cin>>temp>>temp>>temp>>temp;
            else
                cin>>ans2[1]>>ans2[2]>>ans2[3]>>ans2[4];  
        }
        for(int j=1; j<=4; j++)
            for(int k=1; k<=4; k++)
                if(ans[j]==ans2[k])
                    sect.push_back(ans[j]);
            if(sect.size()==0)
                printf("Case #%d: Volunteer cheated!\n", i+1);//cout << "cheated!"<< endl;
            else if(sect.size()>1)
                printf("Case #%d: Bad magician!\n", i+1);//cout << "bad magician" << endl;
            else
                printf("Case #%d: %d\n", i+1, sect[0]);
                
           
    }

    return 0;
}


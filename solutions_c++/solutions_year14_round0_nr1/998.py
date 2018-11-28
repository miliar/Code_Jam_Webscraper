//
//  main.cpp
//  MagicCard
//
//  Created by Tingting Cao on 12/04/2014.
//  Copyright (c) 2014 Tingting Cao. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[])
{
    int case_num;
    cin>>case_num;
    
    for(int c=0;c<case_num;c++)
    {
        //each case
        int first_ans,second_ans;
        vector<vector<int> > cards_first(4);
        vector<vector<int> > cards_second(4);

        cin>>first_ans;
        first_ans--;
        
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int temp;
                cin>>temp;
                cards_first[i].push_back(temp);
            }
        }
        
        cin>>second_ans;
        second_ans--;
        
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int temp;
                cin>>temp;
                cards_second[i].push_back(temp);
            }
        }
        
        //check input
        
//        cout<<first_ans<<endl;
//        for(int i=0;i<cards_first.size();i++)
//        {
//            for(int j=0;j<cards_first[i].size();j++)
//            {
//                cout<<cards_first[i][j]<<" ";
//            }
//            cout<<endl;
//        }
//        
//        cout<<second_ans<<endl;
//        for(int i=0;i<cards_second.size();i++)
//        {
//            for(int j=0;j<cards_second[i].size();j++)
//            {
//                cout<<cards_second[i][j]<<" ";
//            }
//            cout<<endl;
//        }
        
        //calculate output
        
        int ans=0;
        vector<int> secret_num;
        
        for(int i=0;i<4;i++)
        {
            int cur=cards_first[first_ans][i];
            
            //find cur in second ans
            vector<int>::iterator it=find(cards_second[second_ans].begin(), cards_second[second_ans].end(),cur);
            
            if(it!=cards_second[second_ans].end())
            {
                ans++;
                secret_num.push_back(cur);
//                cout<<"Adding one answer "<<cur<<endl;
            }
        }
        
        //check out put
        cout<<"Case #"<<c+1<<": ";
        if(ans==0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else if(ans==1)
        {
            cout<<secret_num[0]<<endl;
        }
        else if(ans>1)
        {
            cout<<"Bad magician!"<<endl;
        }
    }

    return 0;
}


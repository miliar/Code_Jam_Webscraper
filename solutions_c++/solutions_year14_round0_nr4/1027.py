//
//  main.cpp
//  Mass
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
        int block_num;
        cin>>block_num;
        
        vector<double> Naomi;
        vector<double> Ken;
        vector<double> Naomi_Game2;
        vector<double> Ken_Game2;
        
        for(int i=0;i<block_num;i++)
        {
            double temp;
            cin>>temp;
            Naomi.push_back(temp);
            Naomi_Game2.push_back(temp);
        }
        Naomi_Game2=Naomi;
        
        for(int i=0;i<block_num;i++)
        {
            double temp;
            cin>>temp;
            Ken.push_back(temp);
            Ken_Game2.push_back(temp);
        }
        
        
        //sort the input
        
        sort(Naomi.begin(), Naomi.end());
        sort(Naomi_Game2.begin(),Naomi_Game2.end());
        
        sort(Ken.begin(), Ken.end());
        sort(Ken_Game2.begin(),Ken_Game2.end());
        
//        sort(Ken.rbegin(),Ken.rend());
        
        //check input
        
        for(int i=0;i<Naomi.size();i++)
        {
//            cout<<Naomi[i]<<" ";
//            cout<<Naomi_Game2[i]<<" ";
        }
//        cout<<endl;
        
        for(int i =0; i<Ken.size();i++)
        {
//            cout<<Ken[i]<<" ";
//            cout<<Ken_Game2[i]<<" ";
        }
//        cout<<endl;
        
        //calculate scores for normal war game
        
        int Naomi_score=0;
        int Ken_score=0;
        
        for(int i=0;i<Naomi.size();i++)
        {
            double curBlock=Naomi[i];
            double toPlay=-1;
            
            for(int j=0;j<Ken.size();j++)
            {
                if(Ken[j]>curBlock)
                {
                    toPlay=Ken[j];
                    break;
                }
            }
            
            if(toPlay>0)
            {
                vector<double>::iterator it=find(Ken.begin(), Ken.end(), toPlay);
                Ken.erase(it);
                Ken_score++;
            }
            else
            {
                toPlay=Ken[0];
                vector<double>::iterator it=find(Ken.begin(), Ken.end(), toPlay);
                Ken.erase(it);
                Naomi_score++;
            }
        }
        
        
        //calculate score for deceptive war
        
        long Naomi_Score2=0;
        int Ken_Score2=0;
        

        
        for(int i=0;i<Naomi_Game2.size();i++)
        {
            if(Naomi_Game2[i]<Ken_Game2[0])
            {
                //deceipt Ken , sacrifice Ken's largest one
                
//                vector<double>:: iterator it=find(Ken_Game2.begin(),Ken_Game2.end(),Ken_Game2[Ken_Game2.size()-1]);
//                
//                Ken_Game2.erase(it);
                
                Ken_Game2.erase(Ken_Game2.end()-1);
                
               
                
                Ken_Score2++;
            }
            else
            {
                //curBlock is heavier than the first of Ken
                //compare
                Naomi_Score2++;
                
//                vector<double>::iterator it=find(Ken_Game2.begin(),Ken_Game2.end(),Ken_Game2[0]);
//                Ken_Game2.erase(it);
                Ken_Game2.erase(Ken_Game2.begin());
            }
        }
        
        
        cout<<"Case #"<<c+1<<": ";
        cout<<Naomi_Score2<<" "<<Naomi_score<<endl;
    
        
    }
    
    return 0;
}


//
//  main.cpp
//  MineSweeper
//
//  Created by Tingting Cao on 4/12/14.
//  Copyright (c) 2014 ___CIS___. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
void printVectorInt(vector<int> ints);
void printPermutations(vector<int> ints);
void print2DVectorInt(vector<vector<int> > intss);



bool upper(int i, int j, vector<vector<int> > &Pat)
{
    if(i==0)
    {
        return false;
    }
    else if(Pat[i-1][j]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool upperLeft(int i, int j, vector<vector<int> > &Pat)
{
    if(i==0||j==0)
    {
        return false;
    }
    else if(Pat[i-1][j-1]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool upperRight(int i, int j, vector<vector<int> > &Pat)
{
    if(i==0||j==Pat[0].size()-1)
    {
        return false;
    }
    else if(Pat[i-1][j+1]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool leftSide(int i,int j, vector<vector<int> > &Pat)
{
    if(j==0)
    {
        return false;
    }
    else if(Pat[i][j-1]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool rightSide(int i, int j,vector<vector<int> > &Pat)
{
    if(j==Pat[0].size()-1)
    {
        return false;
    }
    else if (Pat[i][j+1]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool down(int i, int j,vector<vector<int> > &Pat)
{
    if(i==Pat.size()-1)
    {
        return  false;
    }
    else if (Pat[i+1][j]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool downLeft(int i, int j,vector<vector<int> > &Pat)
{
    if(i==Pat.size()-1||j==0)
    {
        return false;
    }
    else if(Pat[i+1][j-1]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool downRight(int i, int j,vector<vector<int> > &Pat)
{
    if(i==Pat.size()-1||j==Pat[0].size()-1)
    {
        return false;
    }
    else if(Pat[i+1][j+1]==9)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void getHowManyMinesSurrounding(int i,int j,vector<vector<int> > &Pat)
{
    int num_Mine=0;
    
    if(upper(i, j, Pat))
    {
        num_Mine++;
    }
    
    if(upperLeft(i, j, Pat))
    {
        num_Mine++;
    }
    
    if(upperRight(i, j, Pat))
    {
        num_Mine++;
    }
    
    if(leftSide(i, j, Pat))
    {
        num_Mine++;
    }
    
    if(rightSide(i, j, Pat))
    {
        num_Mine++;
    }
    
    if(down(i, j, Pat))
    {
        num_Mine++;
    }
    
    if(downLeft(i, j, Pat))
    {
        num_Mine++;
    }
    
    if(downRight(i, j, Pat))
    {
        num_Mine++;
    }
    
    Pat[i][j]=num_Mine;
}

void StartReveal(int i,int j,vector<vector<int> > &Pat,vector<vector<bool> > &Seen,int &num_Seen)
{
    Seen[i][j]=true;
    num_Seen++;
    
    //upper
    if(i!=0)
    {
        if(Pat[i-1][j]==0&&Seen[i-1][j]==false)
        {
            StartReveal(i-1, j, Pat, Seen, num_Seen);
        }
        else if(Pat[i-1][j]>0&&Seen[i-1][j]==false)
        {
            num_Seen++;
            Seen[i-1][j]=true;
        }
    }
    
    //upper left
    if(i!=0&&j!=0)
    {
        if(Pat[i-1][j-1]==0&&Seen[i-1][j-1]==false)
        {
            StartReveal(i-1, j-1, Pat, Seen, num_Seen);
        }
        else if (Pat[i-1][j-1]>0&&Seen[i-1][j-1]==false)
        {
            num_Seen++;
            Seen[i-1][j-1]=true;
        }
    }
    
    //upper right
    if(i!=0&&j!=Pat[0].size()-1)
    {
        if(Pat[i-1][j+1]==0&&Seen[i-1][j+1]==false)
        {
            StartReveal(i-1, j+1, Pat, Seen, num_Seen);
        }
        else if (Pat[i-1][j+1]>0&&Seen[i-1][j+1]==false)
        {
            num_Seen++;
            Seen[i-1][j+1]=true;
        }
    }
    
    //left
    if(j!=0)
    {
        if(Pat[i][j-1]==0&&Seen[i][j-1]==false)
        {
            StartReveal(i, j-1, Pat, Seen, num_Seen);
        }
        else if(Pat[i][j-1]>0&&Seen[i][j-1]==false)
        {
            num_Seen++;
            Seen[i][j-1]=true;
        }
    }
    
    //right
    
    if(j!=Pat[0].size()-1)
    {
        if(Pat[i][j+1]==0&&Seen[i][j+1]==false)
        {
            StartReveal(i, j+1, Pat, Seen, num_Seen);
        }
        else if (Pat[i][j+1]>0&&Seen[i][j+1]==false)
        {
            num_Seen++;
            Seen[i][j+1]=true;
        }
    }
    
    //down
    
    if(i!=Pat.size()-1)
    {
        if(Pat[i+1][j]==0&&Seen[i+1][j]==false)
        {
            StartReveal(i+1, j, Pat, Seen, num_Seen);
        }
        else if(Pat[i+1][j]>0&&Seen[i+1][j]==false)
        {
            num_Seen++;
            Seen[i+1][j]=true;
        }
        
    }
    
    //downLeft
    if(i!=Pat.size()-1&&j!=0)
    {
        if(Pat[i+1][j-1]==0&&Seen[i+1][j-1]==false)
        {
            StartReveal(i+1, j-1, Pat, Seen, num_Seen);
        }
        else if (Pat[i+1][j-1]>0&&Seen[i+1][j-1]==false)
        {
            num_Seen++;
            Seen[i+1][j-1]=true;
        }
    }
    
    //downRight
    if(i!=Pat.size()-1&&j!=Pat[0].size()-1)
    {
        if(Pat[i+1][j+1]==0&&Seen[i+1][j+1]==false)
        {
            StartReveal(i+1, j+1, Pat, Seen, num_Seen);
        }
        else if(Pat[i+1][j+1]>0&&Seen[i+1][j+1]==false)
        {
            num_Seen++;
            Seen[i+1][j+1]=true;
        }
    
    }
}

void PrintWinPattern(int r, int c, vector<vector<int> > &Pat)
{
    for(int i=0;i<Pat.size();i++)
    {
        for(int j=0;j<Pat[0].size();j++)
        {
            if(i==r&&j==c)
            {
                cout<<"c";
            }
            else if (Pat[i][j]==9)
            {
                cout<<"*";
            }
            else
            {
                cout<<".";
            }
        }
        cout<<endl;
    }
}

int main(int argc, const char * argv[])
{
//    int myints[]={1,1,1,0,1};
//    
//    sort(myints, myints+5);
//    
//    vector<int> all;
//    all.push_back(3);
//    all.push_back(3);
//    all.push_back(0);
//    
//    sort(all.begin(), all.end());
//    
//    do
//    {
//        for(int i=0;i<all.size();i++)
//        {
//            cout<<all[i]<<" ";
//        }
//        cout<<endl;
//    }
//    while (next_permutation(all.begin(), all.end()));
//    
//    
//    do
//    {
//        cout<<myints[0]<<" "<<myints[1]<<" "<<myints[2]<<endl;
//    }
//    while(next_permutation(myints, myints+3));
//    
//    cout << "After loop: " << myints[0] <<" " << myints[1] << " "<< myints[2] <<endl;
    
    int case_num;
    cin>>case_num;
//    cout<<case_num<<endl;
    
    for(int c=0;c<case_num;c++)
    {
        //each case
        int R,C,M;
        cin>>R>>C>>M;
//        cout<<R<<" "<<C<<" "<<M<<endl;
        
        int none=R*C-M;
        
        vector<int> Initials;
        
        for(int i=0;i<none;i++)
        {
            Initials.push_back(-1);
        }
        
        for(int i=0;i<M;i++)
        {
            Initials.push_back(9);
        }
        
        printVectorInt(Initials);
        
//        printPermutations(Initials);
        
        vector<int> current;
       
        
        bool TriedAll=false;
        bool won=false;
        
        do
        {
            current=Initials;
            
            vector<vector<int> > Patterns(R);
            
            for(int i=0;i<Initials.size();i++)
            {
                int row_num=i/C;
                Patterns[row_num].push_back(Initials[i]);
            }
            
//            cout<<"Initial Pattern"<<endl;
//            print2DVectorInt(Patterns);
            
            for(int i=0;i<Patterns.size();i++)
            {
                for(int j=0;j<Patterns[i].size();j++)
                {
                    if(Patterns[i][j]==-1)
                    {
                        getHowManyMinesSurrounding(i, j, Patterns);
                    }
                }
            }
            
//            cout<<"After ChecKing Surrounding"<<endl;
//            print2DVectorInt(Patterns);
            
            //Start From where it's 0, see whether we can reveal all the none-Mine blocks.
            
            for(int i=0;i<Patterns.size();i++)
            {
                for(int j=0;j<Patterns[i].size();j++)
                {
                    int num_seen=0;
                    
                    if(Patterns[i][j]==0)
                    {
//                      cout<<"Checking "<<Patterns[i][j]<<endl;
                        vector< vector<bool> > Seen(R, vector<bool>(C));
                        StartReveal(i, j, Patterns, Seen, num_seen);
//                        cout<<"Number Seen "<<num_seen<<endl;
                        
                    }
                    else if(Patterns[i][j]!=9)
                    {
//                        cout<<"Checking "<<Patterns[i][j]<<endl;
                        num_seen++;
//                        cout<<"Number Seen "<<num_seen<<endl;
                    }
                    
                    if(num_seen==R*C-M)
                    {
//                        cout<<"Won"<<endl;
                        won=true;
                        cout<<"Case #"<<c+1<<":"<<endl;;
                        PrintWinPattern(i, j, Patterns);
                        break;
                    }
                    else
                    {
                        
                    }
                }
                
                if(won==true)
                {
                    break;
                }
            }
            
            
            if(won==true)
            {
                break;
            }
            
        }
        while (next_permutation(Initials.begin(), Initials.end()));
        
        if(won==false)
        {
            cout<<"Case #"<<c+1<<":"<<endl;
            cout<<"Impossible"<<endl;
        }
    }
    
    
    
    
    return 0;
}

void printVectorInt(vector<int> ints)
{
//    for(int i=0;i<ints.size();i++)
//    {
//        cout<<ints[i]<<" ";
//    }
//    cout<<endl;
}

void printPermutations(vector<int> ints)
{
//    cout<<"Following permutaions:"<<endl;
//    do
//    {
//        printVectorInt(ints);
//    }
//    while (next_permutation(ints.begin(), ints.end()));
}

void print2DVectorInt(vector<vector<int> > intss)
{
//    for(int i=0;i<intss.size();i++)
//    {
//        for(int j=0;j<intss[i].size();j++)
//        {
//            cout<<intss[i][j]<<" ";
//        }
//        cout<<endl;
//    }
}




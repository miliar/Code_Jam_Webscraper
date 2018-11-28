//
//  main.cpp
//  Deceitful_War
//
//  Created by CuiLei on 4/12/14.
//  Copyright (c) 2014 wolfshow. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int d_win(vector<float> &Naomi, vector<float> &Ken, vector<bool> Naomi_b, vector<bool> Ken_b)
{
    int N = Naomi.size();
    int d_win = 0;
    int total = 0;
    int pos_N, pos_K, pos_RK;
    while(total++ < N)
    {
        for(int i = 0; i < N; i++)
        {
            if(!Naomi_b[i])
            {
                pos_N = i;
                break;
            }
        }
        
        for(int i = 0; i < N; i++)
        {
            if(!Ken_b[i])
            {
                pos_K = i;
                break;
            }
        }
        
        if(Naomi[pos_N] < Ken[pos_K])
        {
            for(int i = N - 1; i >= 0;i--)
            {
                if(!Ken_b[i])
                {
                    pos_RK = i;
                    break;
                }
            }
            
            
            Naomi_b[pos_N] = true;
            Ken_b[pos_RK] = true;
            
        }
        else
        {
            d_win++;
            Naomi_b[pos_N] = true;
            Ken_b[pos_K] = true;
        }
    }
    return d_win;
}

int win(vector<float> &Naomi, vector<float> &Ken, vector<bool> Naomi_b, vector<bool> Ken_b)
{
    int N = Naomi.size();
    int win = 0;
    int total = 0;
    int pos_N, pos_K, pos_RK;
    
    while(total++ < N)
    {
        for(int i = 0; i < N; i++)
        {
            if(!Naomi_b[i])
            {
                pos_N = i;
                break;
            }
        }
        
        pos_K = -1;
        for(int i = 0; i < N; i++)
        {
            if(!Ken_b[i] && Ken[i] > Naomi[pos_N])
            {
                pos_K = i;
                break;
            }
        }
        if(pos_K == -1)
        {
            win++;
        }
        else
        {
            Naomi_b[pos_N] = true;
            Ken_b[pos_K] = true;
        }
    }
    
    return win;
}

int main(int argc, const char * argv[])
{

    // insert code here...
    //std::cout << "Hello, World!\n";
    
    int T, N;
    float tmp;
    cin >> T;
    
    vector<float> Naomi, Ken;
    vector<bool> Naomi_b, Ken_b;
    
    for(int ca = 1; ca <= T; ++ca)
    {
        cin >> N;
        
        Naomi.clear();
        Ken.clear();
        
        for(int i = 0 ; i < N; i++)
        {
            cin >> tmp;
            Naomi.push_back(tmp);
            Naomi_b.push_back(false);
        }
        
        for(int i = 0; i < N; i++)
        {
            cin >> tmp;
            Ken.push_back(tmp);
            Ken_b.push_back(false);
        }
        
        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());
        
        int dwin = d_win(Naomi, Ken, Naomi_b, Ken_b);
        int wwin = win(Naomi, Ken, Naomi_b, Ken_b);
        
        cout << "Case #" << ca << ": " << dwin << " " << wwin << endl;
        
    }
    
    return 0;
}


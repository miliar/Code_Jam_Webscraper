//
//  main.cpp
//  Problem A. Senate Evacuation (small)
//
//  Created by Anirudha Paul on 5/8/16.
//  Copyright © 2016 Anirudha Paul. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstdio>
//#include <freopen>

using namespace std;

struct party
{
    int index;
    int number;
};

bool sortby(party x , party y)
{
    if(x.number == y.number)
    {
        return x.index < y.index;
    }
    return x.number > y.number;
}
int main(int argc, const char * argv[])
{
    freopen("/Users/anirudhapaul/Desktop/A-large.in","r",stdin);
    freopen("/Users/anirudhapaul/Desktop/out.txt","w",stdout);
    int test_case ;
    int input;
    int no_of_party;
    scanf("%d", &test_case);
    
    for(int j= 0 ; j < test_case ; j++)
    {
        party man[26];
        scanf("%d", &no_of_party);
        
        for(int i = 0 ; i < no_of_party ;i++)
        {
            //scanf("%d", &input);
            man[i].index = i;
            man[i].number = 0;
        }
        
        for(int i = 0 ; i< no_of_party ; i++)
        {
            scanf("%d", &input);
            man[i].number = input;
        }
        
        printf("Case #%d:", j+1);
        
            sort(man  , man +no_of_party , sortby);
            
            
            while(man[0].number != man[1].number)
            {
                printf(" %c", 'A' + man[0].index);
                man[0].number--;
            }
        for(int i = 2 ; i < no_of_party ; i++)
        {
            while(man[i].number != 0)
            {
                printf(" %c", 'A' + man[i].index);
                man[i].number--;
            }
        }
        
            while(man[0].number != 0)
            {
                printf(" %c%c", 'A' + man[0].index , 'A' + man[1].index);
                man[0].number--;
            }
        
        printf("\n");
    }
    
    
    return 0;
}

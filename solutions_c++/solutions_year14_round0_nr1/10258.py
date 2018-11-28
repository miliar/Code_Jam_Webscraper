

    #include <iostream>
    #include <cstdio>
    #include <map>
    #include <vector>
    #include <string>
    #include <cstdlib>
    #include <algorithm>
    #include <sstream>
    #include <cctype>
    #include <fstream>

    using namespace std;

#define size 4


int main(){


    //freopen("input.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);



    int tst_cases,n_case=1;
    scanf("%d",&tst_cases);


    while(tst_cases--)
    {
        int row1,row2;
        
        scanf("%d",&row1);

        vector <int> grid1(row1);
        

    int current_row=1;
    int temp;
    for(int current_row=1 ; current_row<=size ; ++current_row)
          {
            if(current_row==row1)
               { 
                for (int i = 0; i < size; ++i)
                    scanf("%d",&grid1[i]);

                //scanf("\n");
                }
            else
            {
                for (int i = 0; i < size; ++i)
                    scanf("%d",&temp);
                //cin.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
                //scanf("\n");
            }
   }


scanf("%d",&row2);

vector<int> grid2(row2);

current_row=1;
for(int current_row=1 ; current_row<=size ; ++current_row)
          {
            if(current_row==row2)
               { 
                for (int i = 0; i < size; ++i)
                    scanf("%d",&grid2[i]);

                //scanf("\n");
                }
            else
            {
                for (int i = 0; i < size; ++i)
                    scanf("%d",&temp);
                //cin.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
                //scanf("\n");
            }
   }



sort(grid1.begin(),grid1.end());
sort(grid2.begin(),grid2.end());

//std::vector<int> output(4);

//set_intersection(grid1.begin(),grid1.end(),grid2.begin(),grid2.end(), std::back_inserter(output));

int match=0;
int match_index=0;

for (int i = 0; i < size; ++i)
{
    for (int j = 0; j < size; ++j)
    {
        if(grid1[i]==grid2[j])
            {
                match++;
                match_index=i;
            }
    }
}

    if( match==1 )
        printf("Case #%d: %d\n",n_case,grid1[match_index]);
    else if(match==0)
        printf("Case #%d: Volunteer cheated!\n",n_case);

    else
        printf("Case #%d: Bad magician!\n",n_case);

    n_case++;

}
    return 0;
}
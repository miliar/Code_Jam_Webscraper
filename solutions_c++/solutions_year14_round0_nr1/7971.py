#include <iostream>

void ReadArrangement(int arrangement[4][4]);


int main()
{
    int T;
    int i;
    std::cin>>T;
    for(i = 0; i<T; i++){
        int ans;
        std::cin>>ans;
        ans = ans-1;
        int arrangement[4][4];
        int possibilities[4];
        ReadArrangement(arrangement);
        int m, n;
        for(n = 0; n<4; n++){
            possibilities[n] = arrangement[ans][n];
        }
        std::cin>>ans;
        ans = ans-1;
        ReadArrangement(arrangement);
        int nMatches = 0, latestMatch; 
        for(m = 0; m<4; m++)
        {
            for(n = 0; n<4; n++)
            {
                if(arrangement[ans][m] == possibilities[n])
                {
                    nMatches++;
                    latestMatch = arrangement[ans][m];
                }
            }
        }
        std::cout<<"Case #"<<(i+1)<<": ";
        if(nMatches == 0)
        {
            std::cout<<"Volunteer cheated!"<<std::endl;
        }
        else if(nMatches > 1)
        {
            std::cout<<"Bad magician!"<<std::endl;
        }
        else{
            std::cout<<latestMatch<<std::endl; 
        }
    }
}

void ReadArrangement(int arrangement[4][4])
{
    int m, n;
    for(m = 0; m<4; m++)
    {
        for(n = 0; n<4; n++)
        {
            std::cin>>arrangement[m][n];
        }
    }
}

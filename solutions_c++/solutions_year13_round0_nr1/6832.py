#include<fstream>
#include<iostream>
#include<vector>
#include<string>

using namespace std;

int generate_r(const vector< string > & data)
{      
    bool isFull = true;
    int sum[10]={0};
    for(int i = 0;i < 4;i++)
    {
        for(int j = 0;j<4;j++)
        {
            if(data[i][j]=='.')
            {
                isFull = false;
                break;
            }    
        }    
    }  
    for(int i = 0;i< 4;i++)
    {
        for(int j = 0;j<4;j++)
        {
                sum[i]+=data[i][j];
        }    
    }    
    for(int i = 0;i< 4;i++)
    {
        for(int j = 0;j<4;j++)
        {
                sum[4+i]+=data[j][i];
        }    
    }    
    for(int j = 0;j<4;j++)
    {
            sum[8]+=data[j][j];
            sum[9]+=data[3-j][j];
    }        
    for(int i = 0;i < 10;i++)
    {
        if(sum[i]==3*88+84||sum[i]==4*88)
                return 1;
        if(sum[i]==3*79+84||sum[i]==4*79)
                return 2;
    }    
    if(isFull)return 3;
    else return 4;
}    
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("result.out");
    int totalnum;
    int i = 0;
    fin >> totalnum;
    string str;
    vector< string > da;      
    int j = 0,k = 0; 
    getline(fin,str);
    while(getline(fin,str)&&i<totalnum)
    {
        if(str.size()!=0 && k < 4 )
        {
            da.push_back(str);
            k++;
        }
        else
        {
            k = 0;
            int result = generate_r(da);           
            switch(result)
            {
                case 1:
                    fout << "Case #" << i+1 << ": X won" << endl;
                    break;
                case 2:
                    fout << "Case #" << i+1 << ": O won" << endl;
                    break;                            
                case 3:
                    fout << "Case #" << i+1 << ": Draw" << endl;
                    break;                                                   
                default:
                    fout << "Case #" << i+1 << ": Game has not completed" << endl;      
            }  
            da.clear();
            i++;
        }  
    }               
    system("PAUSE");
    return 0;
}    

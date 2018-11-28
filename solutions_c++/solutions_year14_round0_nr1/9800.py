#include <iostream>
#include <fstream>
using namespace std;
int row[2][16];
int frow[4];

int main()
{
    int times;
    cin>>times;
    for(int x=0; x<times; x++)
    {   int sol;
        int cards = 0;
        for(int m = 0; m <2 ; m++)
        {   if(m==0)
            {
                int choice;
                cin>>choice;
                int cont = 0;
                for(int y = 0 ; y < 16  ; y++)
                    {   
                        
                            cin>>row[m][y];
    
                            if((choice-1)* 4<=y && choice * 4 >y)
                                {
                                    if(cont != 4)
                                    {   
                                        frow[cont] = row[m][y];
                                        cont++;
                                    }
                                }
                        
                    }
            }
            else
            { 
                int choice;
                cin>> choice;
                 for(int y = 0 ; y < 16  ; y++)
                    {
                        cin>>row[m][y];
                        if((choice-1)* 4<=y && choice * 4 >y)
                            for(int l = 0; l < 4 ; l++)
                            { 
                                if(frow[l]==row[m][y])
                                {
                                    sol = frow[l];
                                    cards++;
                                }
                                
                            }
                    }
            }
        }
        ofstream myfile;
        myfile.open("ans.txt",ios::app);
        
        myfile<<"Case #"<<x+1<<": ";
        switch(cards)
        {
            case 0:
                myfile<<"Volunteer cheated!"<<endl;
                break;
            case 1:
                myfile<<sol<<endl;
            break;
            default:
                myfile<<"Bad Magician!"<<endl;
        }
        myfile.close();
    }

    
}
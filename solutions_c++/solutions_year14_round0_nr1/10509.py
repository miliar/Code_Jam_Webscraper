#include<iostream>
#include <fstream>
using namespace std;


int main()
{
    ifstream fromInput("A-small-attempt7.in");
    ifstream fromContainer("testCase.txt");
    ofstream intoContainer("testCase.txt");
    ofstream intoOutput("output.in");

    string testCaseValue;
    int testCase;
    int iterations=0;
//////////////////////////////////////////////////////////////////////
/////getting test case////////////////////////////////////////////
    getline(fromInput,testCaseValue); //read one row string
    intoContainer<<testCaseValue<<endl; //write one row string into new file
    fromContainer>>testCase; //retrieve as int
    cout<<testCase<<endl;

/////////////////////////////////////////////////////////////////////////


    string rowNumber;
    int row;
    string rowValues;
    int values;
    int array[16];
    int temp1[4];
    int temp2[4];




////reading everything into container//////////////////////////////////
    for(int i=0;i<testCase*10;i++)
        {
            getline(fromInput,rowValues); //read row values
            intoContainer<<rowValues<<endl; //write row values into container

        }
///////////////////////////////////////////////////////////////////
        int counter=0;
        int p=1;

        while(iterations!=testCase)
        {
            int i,j;

        getline(fromInput,rowNumber); //read answer to row location
        intoContainer<<rowNumber<<endl; //write one row string into new file
        fromContainer>>row; //retrieve row number as int
        cout<<row<<endl;



        for(i=0;i<16;i++)
        {
              fromContainer>>values; //retrieve numbers in the row
            array[i]=values;
            cout<<values<<" ";
        }

        switch(row)
        {
           case 1:
            for( i=0;i<4;i++)
            {
                temp1[i]=array[i];
            }
            break;

                case 2:
                for(i=4,j=0;i<8,j<4;i++,j++)
                {
                    temp1[j]=array[i];
                    cout<<temp1[j];

                }
                break;

                    case 3:
                    for(i=8, j=0;i<12,j<4;i++,j++)
                    {
                        temp1[j]=array[i];
                    }
                    break;

                        case 4:
                        for(i=12,j=0;i<16,j<4;i++,j++)
                        {
                            temp1[j]=array[i];
                        }
                        break;
            }

            counter++;
//////////////////////////////////////////////////////////////////////
//////////checking second set of 4 rowed numbers/////////////

   getline(fromInput,rowNumber); //read answer to row location
        intoContainer<<rowNumber<<endl; //write one row string into new file
        fromContainer>>row; //retrieve row number as int
        cout<<endl<<row<<endl;



        for(i=0;i<16;i++)
        {
              fromContainer>>values; //retrieve numbers in the row
            array[i]=values;
            cout<<values<<" ";
        }

        switch(row)
        {
           case 1:
            for(i=0;i<4;i++)
            {
                temp2[i]=array[i];
            }
            break;

                case 2:
                for(i=4,j=0;i<8,j<4;i++,j++)
                {
                    temp2[j]=array[i];

                }
                break;

                    case 3:
                    for(i=8,j=0;i<12,j<4;i++,j++)
                    {
                        temp2[j]=array[i];
                        cout<<temp2[j];
                    }
                    break;

                        case 4:
                        for(i=12,j=0;i<16,j<4;i++,j++)
                        {
                            temp2[j]=array[i];
                        }
                        break;
            }
            counter++;
        int matchFound=0,matchValue;
            if(counter==2)
            {
               for(i=0;i<4;i++)
               {
                   for(j=0;j<4;j++)
                   {
                       if(temp1[i]==temp2[j])
                       {
                           matchFound++;
                           matchValue=temp1[i];
                       }

                      else { }
                   }
               }

               if(matchFound==1)
                       {
                          cout<<"Case #"<<p<<": "<<matchValue<<endl;
                          intoOutput<<"Case #"<<p<<": "<<matchValue<<endl;
                          matchFound=0;
                          p++;
                       }
                       else if(matchFound>1)
                       {
                           cout<<"Case #"<<p<<": Bad magician!"<<endl;
                          intoOutput<<"Case #"<<p<<": Bad magician!"<<endl;
                          matchFound=0;
                          p++;
                       }

                       else if(matchFound==0)
                       {
                            cout<<"Case #"<<p<<": Volunteer cheated!"<<endl;
                            intoOutput<<"Case #"<<p<<": Volunteer cheated!"<<endl;
                            matchFound=0;
                            p++;

                       }

            counter=0;
            }

            iterations++;
        }














return 0;
}


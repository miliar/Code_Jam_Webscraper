#include <iostream>
#include <sstream>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{

     ifstream infile;
     ofstream outfile;
	 infile.open ("B-small-attempt0.in");
	 outfile.open ("output_file.in");
	 string T;
	 getline(infile,T);
	 stringstream buffer(T);
	 int X;
	 string line;
	 buffer >> X;
	 string Row;

    for (int i=1 ;i<=X ;i++)
    {
            cout<<i<<endl;
            getline(infile,line);
            int array_num[2];

            char * cstr, *string_num;
            cstr = new char [line.size()+1];
            strcpy (cstr, line.c_str());
            string_num=strtok (cstr," ");
            int c=0;
             while (string_num!=NULL) {
                        stringstream buffer_num(string_num);
                        buffer_num >> array_num[c];
                        string_num=strtok(NULL," ");
                       c++;
                      }

            int lawn_pattern [array_num[0]][array_num[1]];

            int h;
            for(int j=0;j<array_num[0];j++)
            {
                getline(infile,Row);
                char * row, *row_pattern;
                row = new char [Row.size()+1];
                strcpy (row, Row.c_str());
                row_pattern=strtok (row," ");
                h=0;
             while (row_pattern!=NULL) {
                        stringstream buffer_pattern(row_pattern);
                        buffer_pattern >> lawn_pattern[j][h];
                        row_pattern=strtok(NULL," ");
                       h++;
                      }

            }
            int flag1;
            int flag2;
            int row_num;
            int col_num;
            for(int j=0;j<array_num[0];j++)
            {

                for(h=0;h<array_num[1];h++)
                   {
                    flag1=0;
                    flag2=0;


                       if(lawn_pattern[j][h]==1)
                        {
                            row_num=j;
                            col_num=h;
                            int x,y;
                            //can lawn mooer move in this row?
                            for(x=0; x<array_num[1];x++ )
                            {
                                if(lawn_pattern[row_num][x]==2)
                                {
                                    flag1=1;

                                    break;
                                }
                            }
                            //can lawn mower move in this colun
                            for(y=0; y<array_num[0];y++ )
                            {
                                if(lawn_pattern[y][col_num]==2)
                                {
                                    flag2=1;
                                    break;
                                }
                            }
                            if(flag1==1&&flag2==1)

                                break;

                        }


                   }
                        if(flag1==1&&flag2==1)
                            break;



            }
            if(flag1==1&&flag2==1)
                outfile<<"Case #"<<i<<": NO"<<endl;
            else
                outfile<<"Case #"<<i<<": YES"<<endl;

            }

    return 0;
    }



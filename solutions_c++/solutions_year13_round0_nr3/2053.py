        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2011gcj3out.txt");
            ifstream fin ("2011gcj3in.txt");
            
            int t;
            fin >> t;
            
            string table[100];
            
            table[0]="1";
            table[1]="4";
            table[2]="9";
            table[3]="121";
            table[4]="484";
            table[5]="10201";
            table[6]="12321";
            table[7]="14641";
            table[8]="40804";
            table[9]="44944";
            table[10]="1002001";
            table[11]="1234321";
            table[12]="4008004";
            table[13]="100020001";
            table[14]="102030201";
            table[15]="104060401";
            table[16]="121242121";
            table[17]="123454321";
            table[18]="125686521";
            table[19]="400080004";
            table[20]="404090404";
            table[21]="10000200001";
            table[22]="10221412201";
            table[23]="12102420121";
            table[24]="12345654321";
            table[25]="40000800004";
            table[26]="1000002000001";
            table[27]="1002003002001";
            table[28]="1004006004001";
            table[29]="1020304030201";
            table[30]="1022325232201";
            table[31]="1024348434201";
            table[32]="1210024200121";
            table[33]="1212225222121";
            table[34]="1214428244121";
            table[35]="1232346432321";
            table[36]="1234567654321";
            table[37]="4000008000004";
            table[38]="4004009004004";
            
            string a, b;
            
            for(int i=0; i<t; i++)
            {
            fin >> a;
            fin >> b;
            
            int res=0;
            
            for(int j=0; j<39; j++)
            {
            int aux1=0;
            int aux2=0;
            
            if(a.size() < table[j].size())
            aux1=1;
            else
            if(a.size() == table[j].size() && a <= table[j])
            aux1=1;
            
            if(b.size() > table[j].size())
            aux2=1;
            else
            if(b.size() == table[j].size() && table[j] <= b)
            aux2=1;
            
        
            
            res = res + aux1*aux2;
            
            if(aux2 == 0)
            break;
            }
            
        
            
            fout << "Case #" << i+1 << ": " << res << endl;
            }
            
             
            return 0;
            
        }
        
        


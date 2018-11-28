#include <iostream>
#include <string>
#include <map>
#include <cctype>
using namespace std;

char eval ( const std::string& s )
{
   char current = '1';
   bool sign = true;
   std::string s2 = "";
   for(int i = 0; i < s.size(); i++)
   {
      char c = s[i];
      s2 += c;
      if( current == '1' )
      {
         current = c;
      }
      else if( current == c )
      {
         sign = !sign;
         current = '1';
      }
      else if( current == 'i' && c == 'j' )
      {
         current = 'k';
      }
      else if( current == 'i' && c == 'k' )
      {
         current = 'j';
         sign = !sign;
      }
      else if( current == 'j' && c == 'i' )
      {
         current = 'k';
         sign = !sign;
      }
      else if( current == 'j' && c == 'k' )
      {
         current = 'i';
      }
      else if( current == 'k' && c == 'i' )
      {
         current = 'j';
      }
      else if( current == 'k' && c == 'j' )
      {
         current = 'i';
         sign = !sign;
      }
   //   std::cout << "Current: " << current << " " << sign << std::endl;
   }

   if( sign )
      return current;
   else
   {
      if( current == '1')
         return '!';
      else
         return toupper(current);
   }

   return current;
}

char eval(  char s, char c )
{
   bool sign;
   if( s == '1' )
      sign = true;
   else
   {
      if( s == '!' )
         s = '1';
      sign = islower(s);
   }
   char current = tolower(s);
   
   if( current == '1' )
   {
      current = c;
   }
   else if( current == c )
   {
      sign = !sign;
      current = '1';
   }
   else if( current == 'i' && c == 'j' )
   {
      current = 'k';
   }
   else if( current == 'i' && c == 'k' )
   {
      current = 'j';
      sign = !sign;
   }
   else if( current == 'j' && c == 'i' )
   {
      current = 'k';
      sign = !sign;
   }
   else if( current == 'j' && c == 'k' )
   {
      current = 'i';
   }
   else if( current == 'k' && c == 'i' )
   {
      current = 'j';
   }
   else if( current == 'k' && c == 'j' )
   {
      current = 'i';
      sign = !sign;
   }

   if( sign )
      return current;
   else
   {
      if( current == '1' )
         return '!';
      else
         return toupper(current);
   }

   return current;
}

char eval2(  char s, char c )
{
   bool sign;
   if( s == '1' )
      sign = true;
   else
   {
      if( s == '!' )
         s = '1';
      sign = islower(s);
   }
   char current = tolower(s);
   
   if( current == '1' )
   {
      sign = !sign;
      current = c;
   }
   else if( current == c )
   {    
      current = '1';
   }
   else if( current == 'i' && c == 'j' )
   {    
      current = 'k';
   }
   else if( current == 'i' && c == 'k' )
   {
       sign = !sign;
      current = 'j';     
   }
   else if( current == 'j' && c == 'i' )
   {
       sign = !sign;
      current = 'k';      
   }
   else if( current == 'j' && c == 'k' )
   {    
      current = 'i';
   }
   else if( current == 'k' && c == 'i' )
   {
       
      current = 'j';
   }
   else if( current == 'k' && c == 'j' )
   {
      sign = !sign;
      current = 'i';    
   }

   if( sign )
      return current;
   else
   {
      if( current == '1' )
         return '!';
      else
         return toupper(current);
   }

   return current;
}

int main()
{
   /*
   char q = '1';
   while(true)
   {
      char b;
      cin >> b;
      if( b == '0' )
         break;
      q = eval(q, b);
      std::cout << q << std::endl;
   }
   std::cout << islower('!') << std::endl;
   std::string a;
   cin >> a;
   std::cout << eval(a) << std::endl;
   std::cout << eval("jij") << " " << eval("iji") << " " << eval("jijiji") << std::endl;
   */
  
   int n;
   cin >> n;

   for(int i = 0; i < n; i++)
   {
      int x, y;
      cin >> x >> y;
      std::string s;
      cin >> s;
      std::string result = "NO";

      std::string s2 = s;
      for(int j = 0; j < y-1; j++)
      {
         s2 += s;
      }
     

      if( s2.size() >= 3 )
      {
         bool b = false;        
         int counter = 0;
         char e1 = '1';
         char e2;
         char e3 = eval(s);//entire string
          s = s2;
    //     std::cout << "E3: " << e3 << std::endl;
         switch( y % 4 )
         {
         case 1:
            e3 = e3;
            break;
         case 2:
            e3 = '!';
            break;
         case 3:
            e3 = toupper(e3);
            break;
         case 0:
            e3 = '1';
            break;
         }
         char e32 = e3;
    //     std::cout << "E3: " << e3 << std::endl;
         for(int j = 1; j <= s.size() - 2; j++)
         {  
            e2 = '1';
            e1 = eval(e1,s[j-1]);
            e32 = eval2(e32,s[j-1]);
            e3 = e32;
            if( e1 != 'i' )
            {
       //        std::cout << "e1: " << e1 << std::endl;
               continue;
            }
            else
            {
         //      std::cout << "e1: " << e1 << std::endl;
            }
            for( int k = j+1; k <= s.size() - 1; k++)
            { 
         //      std::cout << s.substr(j,k-(j)) << " " << s.substr(k) << std::endl;
         //      std::cout << e2 << " " << e3 << " " << s[k-1] << std::endl;
               e2 = eval(e2,s[k-1]);
               e3 = eval2(e3,s[k-1]);
      //         std::cout << e2 << " " << e3 << std::endl;
               if( e2 == 'j' && e3 == 'k')
               {
                  b=true;
                  result = "YES";
            //      std::cout << s.substr(0,j) << " " << s.substr(j,k-j) << " " << s.substr(k) << std::endl;
           //       std::cout << eval( s.substr(0,j) ) << " " << eval( s.substr(j,k-j) ) << " " << eval( s.substr(k) ) << std::endl;
                  break;
               }

               counter++;
            }
            if( b )
               break;        
         }

      }
      std::cout << "Case #" << i+1 << ": " << result << std::endl;
   }

}
// FairandSquare.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include "InputFileReader.h"
#include <algorithm>
#include <limits>
#include <conio.h>
using namespace std;


class FaS:public InputFileReader
{
public:
	FaS(string fileName)
		: InputFileReader(fileName)
		, m_field()
	{
  		m_field.push_back(0);
		m_field.push_back(1);
		m_field.push_back(4);
		m_field.push_back(9);
		//m_field.push_back(121);
		//m_field.push_back(484);
		//m_field.push_back(10201);
		//m_field.push_back(12321);
		//m_field.push_back(14641);
		//m_field.push_back(40804);
		//m_field.push_back(44944);
		long long tempValue;
		char buffer [50];
		string str;
      


      m_rowPalindroms.push_back(0);
		for (int i = 1; i < 10; i ++)
		{
			tempValue = i * 10 + i;
         m_rowPalindromsOdd.push_back(tempValue);
			tempValue *= tempValue;
         if (isPalindrom(tempValue))
         {
            m_field.push_back(tempValue);
         }
		}

		for (int i = 0; i < 10; i ++)
		{
			tempValue = i * 100 + i;
			for (int j = 0; j < 10; j++)
			{
				int newValue = tempValue + j*10;
            m_rowPalindromsOdd.push_back(newValue);
            if (i != 0)
            {
               newValue *= newValue;
               if (isPalindrom(newValue))
               {
                  m_field.push_back(newValue);
               }
            }
			}
		}
      addPalindrom(1000, m_rowPalindromsOdd);
      addPalindrom(10000, m_rowPalindroms);
      sort(m_field.begin(), m_field.end());

//       for (int k = 0; k < m_field.size(); k++)
//       {
//          cout << m_field[k] << endl;
//       }
	}

   void addPalindrom(long long multipl, vector <long long> & rowPal)
   {
      if (multipl > 10000000)
      {
         return;
      }
      vector<long long> newRowPal;
      for (int j= 0; j < rowPal.size(); j++)
      {
         for (int i = 0; i < 10; i++)
         {
            long long tempValue = rowPal[j] * 10 + i + i*multipl;
            newRowPal.push_back(tempValue);
            if (i != 0)
            {
               tempValue *= tempValue;
               if (isPalindrom(tempValue))
               {
                  m_field.push_back(tempValue);
               }
            }
         }
      }
      addPalindrom(multipl*100, newRowPal);
   }
   
   bool isPalindrom(long long newValue)
   {
      stringstream ss;
      ss << newValue;
      for (int i = 0, j = ss.str().size()-1; i < j; i++, j--)
      {
         if (ss.str()[i] != ss.str()[j])
         {
            return false;
         }
      }
      return true;
   }


	virtual void readTestCase( std::ifstream & file, std::ofstream & fileOut, int i ) 
	{
		//init play field
//		m_field.clear();
		vector <long long> fieldSize;
		readValue(file, fieldSize);
      unsigned long long int val= std::numeric_limits<unsigned long long int>::max();
      int count = 0;
      while (val > 0)
      {
         count++;
         val /=10;
      }
       //std::cout << "\nint is signed: " << count << '\n';
	 //cout << *lower_bound(m_field.begin(), m_field.end(), fieldSize[1]+1) << " " << *lower_bound(m_field.begin(), m_field.end(), fieldSize[0]);

 		fileOut << "Case #" << i+1 << ": ";
 		fileOut << (lower_bound(m_field.begin(), m_field.end(), fieldSize[1]+1) - lower_bound(m_field.begin(), m_field.end(), fieldSize[0]));
 		fileOut << endl;
	}
	vector <long long> m_field;
   vector <long long> m_rowPalindromsOdd;
   vector <long long> m_rowPalindroms;


};



int _tmain(int argc, _TCHAR* argv[])
{
	FaS fr("c:\\jam.in");
	fr.readFile();
//getch();
	return 0;
}


#include <iostream>
#include <string>
#include <vector>

int nextParty(std::vector<int> const & ppp, int index)
{
   index += 1;
   index = index % ppp.size();

   while(ppp[index] == 0)
   {
      index += 1;
      index = index % ppp.size();
   }

   return index;
}

std::string solveCase()
{
   int numParties;
   std::cin >> numParties;

   std::vector<int> peoplePerParty;
   int numPeople = 0;
   for(int i = 0; i < numParties; i++)
   {
      int temp;
      std::cin >> temp;
      peoplePerParty.push_back(temp);
      numPeople += temp;
   }

   std::vector<std::string> revEvacOrder;
   int curPartyIndex = 0;
   char party;
   while(numPeople > 0)
   {
      std::string curEvac;

      curPartyIndex = nextParty(peoplePerParty, curPartyIndex);

      party = 'A' + curPartyIndex;
      curEvac.push_back(party);
      numPeople--;
      peoplePerParty[curPartyIndex] = peoplePerParty[curPartyIndex] - 1;

      if (numPeople == 0)
      {
         revEvacOrder.push_back(curEvac);
         continue;
      }

      curPartyIndex = nextParty(peoplePerParty, curPartyIndex);

      party = 'A' + curPartyIndex;
      curEvac.push_back(party);
      revEvacOrder.push_back(curEvac);
      numPeople--;
      peoplePerParty[curPartyIndex] = peoplePerParty[curPartyIndex] - 1;
   }

   bool first = true;
   std::string solution;
   for(auto it = revEvacOrder.rbegin(); it != revEvacOrder.rend(); it++)
   {
      if (!first)
      {
         solution += " ";
      }
      else
      {
         first = false;
      }

      solution += *it;
   }


   return solution;

}

int main(int, char**)
{
   int numCases = 0;
   std::cin >> numCases;

   for(int i = 0; i < numCases; i++)
   {
      std::cout << "Case #" << i+1 << ": " << solveCase() << std::endl;
   }

   return 0;
}

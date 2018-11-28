In[155]:= 
txt = Import[
   "C:\\Users\\Emile \
Okada\\Documents\\Mathematica\\codejam\\A-large.in.txt"];

In[158]:= 
tTxt = Delete[
   StringSplit[#, ""] & /@ StringSplit[#, "\n"] & /@ 
    StringSplit[txt, "\n\n"], {1, 1}];

In[145]:= 
test[x_] := If[! MemberQ[x, "."], Equal @@ Cases[x, Except["T"]]]

In[101]:= 
genLines[list_] := 
 Join[{Diagonal@list}, {Diagonal[Reverse /@ list]}, list, 
  list\[Transpose]]

In[130]:= 
check[list_] := 
 If[Length@# != 0, If[MemberQ[#, "O", -1], "O won", "X won"], 
    If[MemberQ[list, ".", -1], "Game has not completed", "Draw"]] &@
  Cases[genLines[list], _?test]

In[159]:= Export["C:\\Users\\Emile \
Okada\\Documents\\Mathematica\\codejam\\ansLarge.txt", 
 StringJoin["Case #", ToString@First@#2, ": ", check@#] &~MapIndexed~
  tTxt]

Out[159]= "C:\\Users\\Emile \
Okada\\Documents\\Mathematica\\codejam\\ansLarge.txt"